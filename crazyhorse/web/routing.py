import re
import os
import weakref
from crazyhorse.web import exceptions
from crazyhorse.utils.tools import import_class

def register_route(name, controller, action, path, method="GET", constraints=None):
    route = Route(path, constraints)
    route.register_action_for_method(method, controller, action)
    application_router.add_route(name, route, method)
    return route

class Router(object):

    def __init__(self):
        self.route_table      = []
        self.routes_available = {}

    def add_route(self, name, route, method):
        """Add a route to the respective route collections"""
        if name not in self.routes_available:
            self.routes_available[name] = route
            self.route_table.append(route)
        else:
            controller, action = route.actions[method]
            raise exceptions.DuplicateRouteNameException(name, controller, action)

    def route_with_name(self, route_name):
        """Find a route based on the provided name"""
        try:
            route = self.routes_available[route_name]
        except:
            raise exceptions.InvalidRouteNameException(route_name)

        return route

    def route_for_path(self, path):
        """Find a route based on the provided path, ignores query string values"""
        route = None

        for candidate in self.route_table:
            if candidate.pattern.match(path):
                route = candidate
                break

        if route is None:
            raise exceptions.InvalidRoutePathException(path)

        return route


class Route(object):
    # Note that the params test excludes periods.
    params_test = re.compile(r"\{([a-zA-Z0-9_]+)\}")

    def __init__(self, path=None, constraints=None):
        self.actions     = {}
        self.pattern     = None
        self.params      = None
        self.path        = path
        self.constraints = constraints

        if path is not None:
            pattern         = None
            params          = None

            if Route.params_test.search(path):
                params  = tuple(Route.params_test.findall(path))
                if constraints is not None:
                    pattern = path
                    for key in Route.params_test.findall(path):
                        if key in constraints:
                            pattern = re.sub(r"{" + key + r"}", "(" + constraints[key] + ")", pattern )
                else:
                    pattern = Route.params_test.sub(r"([^/]+)", path)
            else:
                pattern = path
            
            # if the path is a directory, eg:
            # /foo/bar
            # we want crazyhorse to also match /foo/bar/
            # if we find a "." in the basename this points us to a file
            # so don't add an optional /? to the regex.
            # if the ValueError is raised, no "." was found
            # so we have a /foo/bar situation. In that case 
            # also match /foo/bar/?
            
            extra = ""
            
            try:
                os.path.basename(path).rindex(".")
            except ValueError:
               extra = "/?"

            try:
                self.pattern = re.compile("^" + pattern + extra + "$")
            except Exception:
                raise exceptions.InvalidConstraintException(pattern)

            if params is not None: self.params = params

    def register_action_for_method(self, method, controller, action, temp=False):
        method = method.upper().strip()
        self.actions[method] = (controller, action)

    def action_with_method(self, method):
        try:
            return self.actions[method]
        except KeyError as e:
            if "*" in self.actions:
                return self.actions["*"]
            else:
                if "GET" in self.actions:
                    return self.actions["GET"]
                else:
                    raise e

    def __call__(self, context):
        path       = context.path
        method     = context.method
        controller = None
        action     = None
        cls        = None
        result     = None

        try:
            controller, action = self.action_with_method(method)
        except KeyError as e:
            raise exceptions.RouteExecutionException(path, e.message)

        if controller not in route_controller_registry:
            cls = import_class(controller)
            route_controller_registry[controller] = cls
        else:
            cls = route_controller_registry[controller]

        params = {}

        if self.params:
            result = self.pattern.match(path)
            params = dict(zip(self.params, result.groups()))

        obj = cls(context)
        
        try:
            init = getattr(obj, "initialize")
            init(context.request)
        except KeyError:
            # initialize is optional
            pass
        
        method = getattr(obj, action)
        
        try:
            result = method(**params)

            if result is not None:
                result._httpcontext = context

        except exceptions.RouteAuthorizationException:
            raise
        except Exception as e:
            raise exceptions.RouteExecutionException(path, "{0} in {1}.{2}".format(e.message, controller, action))
        
        return result

temp_routes               = {}
route_controller_registry = {}
application_router        = Router();