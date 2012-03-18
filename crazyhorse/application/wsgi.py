import sys
from os.path import normpath
import crazyhorse
from crazyhorse.application import CrazyHorseExecutionContext
from crazyhorse.configuration.manager import Configuration
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.results import NotFoundResult
from crazyhorse.web.results import ServerErrorResult
from crazyhorse.web.results import ForbiddenResult
from crazyhorse.web import exceptions
from crazyhorse.web import routing

class Application(object):

    def __init__(self, application):
        
        # fire it up!
        self.application = application
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        crazyhorse.get_logger().debug("Processing Configuration")
        Configuration()

        crazyhorse.get_logger().debug("Executing custom application_start")
        application.application_start()
        

    def __call__(self, environ, start_response):
            route            = None
            context          = None
            path             = environ["PATH_INFO"]
            router           = routing.application_router

            # paths in the router are normalzied to not end with a /
            # so we apply the same rule here
            path = normpath(path)
            #if len(path) > 1 and path[-1:] is "/":
            #    path = path[:-1]

            # we have a route object, lets get busy:
            httpcontext = HttpContext(environ, start_response)
            application_features = Configuration.CRAZYHORSE_FEATURES
            controller_factory   = Configuration.CRAZYHORSE_CONTROLLER_FACTORY
            
            crazyhorse_context = CrazyHorseExecutionContext(self.application, 
                                                            application_features,
                                                            httpcontext,
                                                            controller_factory)

            with crazyhorse_context as ctx:
                context            = ctx.httpcontext
                controller_factory = ctx.controller_factory

                try:
                    route = router.route_for_path(path)
                except exceptions.InvalidRoutePathException:
                    try:
                        route = router.route_with_name("404")
                    except exceptions.InvalidRouteNameException as e:
                        # No 404 override route, we are done here
                        result = NotFoundResult()
                        result._httpcontext = context
                        context.response.result = result
                        return context

                # -------- testing stuff
                #print(environ)
                #content_length = -1
                #try:
                #    content_length = int(context.environ.get("CONTENT_LENGTH", "0"))
                #except ValueError:
                #    pass
                #
                #if "wsgi.input" in environ:
                #    print(content_length)
                #    data = environ["wsgi.input"].read(content_length)
                #    f = open("multipart-request.txt", "wb")
                #    f.write(data)
                #    #environ["wsgi.input"].seek(0)
                #
                #    start_response("200 Ok", [])
                #    return []
                # --------


                # TODO I think I can make this nicer
                # Feels a little sloppy to me

                try:
                    context.response.result = route(context, controller_factory)
                except exceptions.RouteExecutionException as e:
                    crazyhorse.get_logger().error(e.message)
                    #tb = sys.exc_info()[2]
                    #traceback.print_tb(tb, limit=5, file=sys.stdout)
                    #del tb

                    try:
                        route = router.route_with_name("500")
                        context.response.result = route(context, controller_factory)

                    except (exceptions.InvalidRouteNameException, exceptions.RouteExecutionException) as e:
                        # No 500 route, or it failed, in either case we are done here
                        result = ServerErrorResult()
                        result._httpcontext = context
                        context.response.result = result
                        return context
                
                except exceptions.RouteAuthorizationException as e:
                    #crazyhorse.get_logger().error(e.message)

                    try:
                        route = router.route_with_name("authorization." + e.provider_name)
                        context.response.result = route(context, controller_factory)
                    except (exceptions.InvalidRouteNameException, exceptions.RouteExecutionException) as e:
                        # No authorization error route, or it failed, in either case we are done here
                        result = ForbiddenResult()
                        result._httpcontext = context
                        context.response.result = result
                        return context

                return context
            #end context manager