class ConfigurationErrorException(Exception):

    def __init__(self, value):
        self.message = "Invalid crazyhourse.config: {0}".format(value)


class DuplicateRouteNameException(Exception):

    def __init__(self, route_name, controller, action):
        self.message = "Route at {0}.{1} is using a duplicate name: {2}".format(controller, action, route_name)

class InvalidConstraintException(Exception):

    def __init__(self, pattern):
        self.message = "Invalid route constraint. Unable to compile regex {0}".format(pattern)

class InvalidRouteNameException(Exception):

    def __init__(self, route_name):
        self.message = "Invalid route unable to locate existing route with name: {0}".format(route_name)

class InvalidRoutePathException(Exception):

    def __init__(self, path):
        self.message = "Invalid route unable to locate existing route for path: {0}".format(path)

class RouteExecutionException(Exception):

    def __init__(self, path, message):
        self.message  = "Executing route for {0} failed: {1}".format(path, message)

class RouteAuthorizationException(Exception):

    def __init__(self, provider_name, message=""):
        self.provider_name = provider_name
        self.message  = "Authorization failed. {0}".format(message)

