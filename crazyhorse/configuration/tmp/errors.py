from crazyhorse.web import routing
class ConfigurationErrors(object):

    def initialize_application_errors(self, config):
            #error is an ElementTree.Element
            router = routing.application_router

            for error in config.server_errors.errors:
                controller = error["controller"]
                action     = error["action"]
                code       = error["code"]
                method     = error["method"]

                route      = None

                try:
                    route  = router.routes_available[code]
                except:
                    route = routing.Route()
                    router.routes_available[code] = route

                if method == "*":
                    route.register_action_for_method("*", controller, action)
                else:
                    method_list = method.split(",")
                    for target_method in method_list:
                        route.register_action_for_method(target_method, controller, action)