import crazyhorse

from crazyhorse.configuration import Configuration
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web import exceptions
from crazyhorse.web import routing

class Application():

    def __init__(self, application=None):
        #self.router         = options["router"]() if "router" in options else None
        #self.authorization  = options["authorization"]() if "authorization" in options else None
        #self.sessions       = options["sessions"] if "sessions" in options else None
        #self.cookies        = options["cookies"] if "cookies" in options else None
        #self.request_parser = options["request_parser"] if "request_parser" in options else None
        #self.views          = options["views"] if "views" in options else None


        # fire it up!
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        Configuration()
        return
        if application is not None:
            application_start = getattr(application, "application_start", None)

            if application_start:
                crazyhorse.get_logger().debug("Executing custom application_start")
                application_start()



    def __call__(self, environ, start_response):

            request_handlers = {}
            route            = None
            context          = HttpContext(environ, start_response)
            router           = routing.application_router
            try:
                route = router.route_for_path(context.request.path)
            except (exceptions.InvalidRoutePathException):
                try:
                    route = router.route_with_name("404")
                except:
                    start_response("404 NOT FOUND", [])
                    return []

            try:
                route(context)
            except (exceptions.RouteExecutionException):
                start_response("404 NOT FOUND", [])
                return []
            #context.request     = Request(environ, request_handlers)
            #context.response    = Response(start_response)
            start_response("200 OK", [])
            return ["It Works!"]

            handlers = {"environ":environ,
                        "request_parser": self.request_parser,
                        "cookies":self.cookies,
                        "session":self.sessions}

            context             = HttpContext()
            context.request     = Request(**handlers)
            context.response    = Response(start_response, self.cookies)
            context.session     = None if self.sessions is None else  self.sessions(context.request)
            context.view_engine = self.views
            context.environ     = environ

            result = None
            route  = router.fetch_route(context)

            #if route.controller.requires_authorization and self.authorization is not None:
            #    if self.authorization.request_is_authorized(request) is False:


            if route is not None:
                route.context = context
                result = route()
            else:
                return
            return context.response(session=context.session, result=result)