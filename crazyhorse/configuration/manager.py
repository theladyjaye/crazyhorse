from __future__ import absolute_import
import os
import json
import importlib
import collections
import crazyhorse
from crazyhorse.web import exceptions
from crazyhorse.configuration.application import ApplicationSection
from crazyhorse.configuration.routes import ApplicationRoutesSection
from crazyhorse.configuration.crazyhorse import CrazyHorseSection
from crazyhorse.utils.tools import import_class


class Configuration(object):

    APP_SETTINGS                = None
    APP_AUTHORIZATION_PROVIDERS = None
    CRAZYHORSE_FEATURES         = None

    def __init__(self):
        with open(os.getcwd() + "/crazyhorse.config") as config_json:
            try:
                config      = json.load(config_json)
                self.initialize_sections(config)
            except ValueError as e:
                crazyhorse.get_logger().fatal("Unable to decode crazyhorse.config: {0}".format(str(e)))
            except exceptions.DuplicateRouteNameException as e:
                crazyhorse.get_logger().fatal("Duplicate route name defined: {0}".format(e.message))
            except Exception as e:

                crazyhorse.get_logger().fatal("Error parsing config: {0}".format(str(e)))

    def initialize_sections(self, config):
        application_section        = ApplicationSection()
        application_routes_section = ApplicationRoutesSection()
        application_config         = None

        try:
            application_config = config["application"]
        except KeyError:
            crazyhorse.get_logger().fatal("No application section defined in config")
            raise exceptions.ConfigurationErrorException("No application section defined in config")
        
        processed_results                         = application_section(application_config)
        Configuration.APP_SETTINGS                = processed_results["settings"]
        Configuration.APP_AUTHORIZATION_PROVIDERS = processed_results["authorization_providers"]
        
        application_routes_section(application_config)

        self.initialize_crazyhorse_features(config)

        if "custom_sections" in config:
            for custom_section in config["custom_sections"]:
                self.initialize_custom_section(config, custom_section)
    
    def initialize_crazyhorse_features(self, config):
        try:
            crazyhorse_section         = CrazyHorseSection()
            Configuration.CRAZYHORSE_FEATURES = crazyhorse_section(config["crazyhorse"])
        except KeyError:
            crazyhorse.get_logger().fatal("No crazyhorse section defined in config")
            raise exceptions.ConfigurationErrorException("No crazyhorse section defined in config")

    def initialize_custom_section(self, config, meta):

        name    = meta["name"]
        pkg     = meta["type"]
        cls     = import_class(pkg)
        obj     = None
        section = None

        crazyhorse.get_logger().debug("Processing {0} Configuration".format(cls.__name__))

        if name in config:
            section = config[name]

        obj = cls()

        config_name = "CUSTOM_" + name.upper().replace("-", "_")

        if section:
            setattr(Configuration, config_name, obj(section))
        else:
            setattr(Configuration, config_name, obj())
