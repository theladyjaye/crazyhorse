from __future__ import absolute_import
import crazyhorse
from crazyhorse.utils.tools import import_class
from crazyhorse.configuration.sections import ConfigurationSection

class CrazyHorseFeatureCollection(object):
    def __init__(self):
        self._features = []

    def register(self, feature):
        self._features.append(self.load_feature(feature))

    def register_authentication(self, feature):
        self.authenticate = self.load_feature(feature)

    def load_feature(self, pkg):
        obj = import_class(pkg)
        return obj

    def __iter__(self):
        return iter(self._features)

class CrazyHorseSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_controller_factory(self, qualified_name):
        # there is an import error that necessitates this import 
        # statement here. If we place it above, an error is thrown
        from crazyhorse.configuration.manager import Configuration
        cls = import_class(qualified_name)
        Configuration.CRAZYHORSE_CONTROLLER_FACTORY = cls()

    def initialize_features(self, section):
        #order is important here when it comes to cookies / sessions
        #sessions must always be initialized AFTER cookies.
        #result = {}
        features = CrazyHorseFeatureCollection()

        if "request_body" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Request Body")
            #result["request_body"] = self.load_feature(section["request_body"])
            features.register(section["request_body"])

        if "querystrings" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Query Strings")
            features.register(section["querystrings"])
        
        if "cookies" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Cookies")
            features.register(section["cookies"])

        # needs to go after cookies, cookies must be initialized first.
        if "sessions" in section:
            if "cookies" not in section:
                crazyhorse.get_logger().critical("Attempt to enable Sessions without enabling Cookies")
            else:
                crazyhorse.get_logger().debug("Feature Enabled: Sessions")
                features.register(section["sessions"])

        if "authentication" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Authentication")
            features.register_authentication(section["authentication"])

        return features

    def __call__(self, section):

        crazyhorse.get_logger().debug("Processing CrazyHorse Configuration")
        features = None

        try:
            features = self.initialize_features(section["features"])
        except KeyError:
            crazyhorse.get_logger().critical("No crazyhorse features defined in config")

        try:
            self.initialize_controller_factory(section["controller_factory"])
        except KeyError:
            crazyhorse.get_logger().critical("No controller factory defined in config")

        return features
