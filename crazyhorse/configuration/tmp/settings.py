import glob
import os
import crazyhorse
from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web import routing
from crazyhorse.web import exceptions


class ConfigurationSettings(object):

    def initialize_application_settings(self, config):
        self.initialize_application_default_view(config)
        self.initialize_application_controllers(config)


    def initialize_application_default_view(self, config):
        view_path = None
        try:
            view_path        = config.settings["default_view"]
        except KeyError:
            crazyhorse.get_logger().warning("No default_view specified in config. Calling MyController.view() will throw error")
            return

        parts            = view_path.split(".")
        view_classname   = parts.pop()
        view_module_path = ".".join(parts)

        crazyhorse.get_logger().debug("importing default view {0}".format(view_module_path + "." + view_classname))

        view_module      = __import__(view_module_path, globals(), locals(), [str(view_classname)])

        view_class       = getattr(view_module, view_classname)
        CrazyHorseController.view_class = view_class

    def initialize_application_controllers(self, config):
        controllers_path = None
        try:
            controllers_path = config.settings["controllers"]
        except KeyError:
            crazyhorse.get_logger().fatal("No controller module defined in config")
            raise exceptions.ConfigurationErrorException("No controllers module defined in settings")

        controllers_path = controllers_path.replace(".", "/")

        #process controllers for any routes
        for file_path in glob.iglob("{0}/*.py".format(controllers_path)):

            if os.path.basename(file_path).startswith("__"): continue

            file_path     = os.path.splitext(file_path)[0]
            module_path   = file_path.replace("/", ".")
            crazyhorse.get_logger().debug("processing routes within controller {0}".format(module_path))
            module        = __import__(module_path, globals(), locals())

    def process_orphaned_routes(self):
        router = routing.application_router
        if len(routing.temp_routes) > 0:
            for route_name in routing.temp_routes:
                try:
                    route = router.route_with_name(route_name)
                    for method in routing.temp_routes[route_name]:
                        controller, action  = routing.temp_routes[route_name][method]
                        route.register_action_for_method(method, controller, action)
                except:
                    temp_route = routing.temp_routes[route_name]
                    for key in temp_route.iterkeys():
                        crazyhorse.get_logger().warning("Failed to register route for with name: {0} for {1}::{2}".format(route_name, temp_route[key][0], temp_route[key][1]))

        del routing.temp_routes
        #routing.temp_routes = None