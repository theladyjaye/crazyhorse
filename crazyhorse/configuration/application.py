import glob
import os
import json
import crazyhorse
from crazyhorse.utils.tools import import_class
from crazyhorse.utils.tools import import_module
from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.configuration.sections import ConfigurationSection
from crazyhorse.web import routing
from crazyhorse.web import exceptions

class ApplicationSection(ConfigurationSection):

    def initialize_authorization_providers(self, authorization_providers):
        crazyhorse.get_logger().debug("Initializing Authorization Providers")
        providers = {}
        
        for provider in authorization_providers:
            name     = None
            package  = provider["provider"]

            try:
                name = provider["name"]
            except KeyError:
                name = "default"

            cls = import_class(package)
            
            if cls:
                providers[name] = cls()
                continue
            
            crazyhorse.get_logger().fatal("Failed to import authorization provider: {0}.".format(package))
            raise exceptions.ConfigurationErrorException("Failed to import authorization provider")
        
        return providers

    #views should contain their content-type definition for the response
    def initialize_default_view(self, section):

        view_path = None
        try:
            view_path        = section["default_view"]
        except KeyError:
            crazyhorse.get_logger().warning("No default_view specified in config. Calling MyController.view() will throw error")
            return

        crazyhorse.get_logger().debug("Registering default view: {0}".format(view_path))

        cls = import_class(view_path)

        if cls:
            CrazyHorseController.view_class = cls
            return

        crazyhorse.get_logger().fatal("Failed to import specified default view: {0}. Calling MyController.view() will throw error".format(view_path))
        raise exceptions.ConfigurationErrorException("Failed to import specified default view")


    def __call__(self, section):
        crazyhorse.get_logger().debug("Processing Application Configuration")
        settings = None
        authorization_providers = None
        result = {}

        if "settings" in section:
            result["settings"] = section["settings"]
        
        if "authorization_providers" in section:
            result["authorization_providers"] = self.initialize_authorization_providers(section["authorization_providers"])
        
        try:
            self.initialize_default_view(section["system"])
        except KeyError:
            crazyhorse.get_logger().fatal("No system section defined in application config")
            raise exceptions.ConfigurationErrorException("No system section defined in application config")

        return result