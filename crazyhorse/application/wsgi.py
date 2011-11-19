import crazyhorse
from crazyhorse.configuration.manager import Configuration
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.response import ResponseStatus
from crazyhorse.web import exceptions
from crazyhorse.web import routing

class Application(object):

    def __init__(self, application=None):
        
        # fire it up!
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        crazyhorse.get_logger().debug("Processing Configuration")
        Configuration()

        if application is not None:
            application_start = getattr(application, "application_start", None)

            if application_start:
                crazyhorse.get_logger().debug("Executing custom application_start")
                application_start()


    def __call__(self, environ, start_response):
            route            = None
            context          = None
            path             = environ["PATH_INFO"]
            router           = routing.application_router

            try:
                route = router.route_for_path(path)
            except exceptions.InvalidRoutePathException:
                try:
                    route = router.route_with_name("404")
                except exceptions.InvalidRouteNameException:
                    # No 404 route, we are done here
                    start_response(ResponseStatus.NOT_FOUND, [])
                    return []


            # we have a route object, lets get busy:
            context = HttpContext(environ, start_response)

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

            # apply features
            application_features = Configuration.CRAZYHORSE_FEATURES
            [x(context) for x in application_features]


            # TODO I think I can make this nicer
            # Feels a little sloppy to me

            try:
                context.response.result = route(context)
                print(1)
            except exceptions.RouteExecutionException as e:
                crazyhorse.get_logger().error(e.message)
                
                try:
                    route = router.route_with_name("500")
                    context.response.result = route(context)
                    print(2)
                except exceptions.InvalidRouteNameException, exceptions.RouteExecutionException:
                    # No 500 route, or it failed, in either case we are done here
                    start_response(ResponseStatus.SERVER_ERROR, [])
                    print(3)
                    return []
            
            except exceptions.RouteAuthorizationException as e:
                #crazyhorse.get_logger().error(e.message)
                print(4)

                try:
                    route = router.route_with_name("authorization." + e.provider_name)
                    context.response.result = route(context)
                    print(5)
                except exceptions.InvalidRouteNameException, exceptions.RouteExecutionException:
                    # No authorization error route, or it failed, in either case we are done here
                    start_response(ResponseStatus.FORBIDDEN, [])
                    print(6)
                    return []

            return context