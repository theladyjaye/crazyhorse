from __future__ import absolute_import
import crazyhorse
from crazyhorse.configuration.sections import ConfigurationSection
from crazyhorse.utils.tools import import_class

class CrazyHorseSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_features(self, section):
        result = {}

        if "request_body" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Request Body")
            result["request_body"] = self.load_feature(section["request_body"])

        if "sessions" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Sessions")
            result["sessions"] = self.load_feature(section["sessions"])

        if "cookies" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Cookies")
            result["cookies"] = self.load_feature(section["cookies"])

        if "querystrings" in section:
            crazyhorse.get_logger().debug("Feature Enabled: Query Strings")
            result["querystrings"] = self.load_feature(section["querystrings"])

        return result

    def load_feature(self, pkg):
        obj = import_class(pkg)
        return obj

    def __call__(self, section):

        crazyhorse.get_logger().debug("Processing CrazyHorse Configuration")
        features = None

        try:
            features = self.initialize_features(section["features"])
        except KeyError:
            crazyhorse.get_logger().critical("No crazyhorse features defined in config")

        return features
