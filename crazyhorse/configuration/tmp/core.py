from crazyhorse.configuration.settings import ConfigurationSettings
from crazyhorse.configuration.handlers import ConfigurationHandlers
from crazyhorse.configuration.errors import ConfigurationErrors
from crazyhorse.configuration.system import ConfigurationSystem
from crazyhorse.web.config import CrazyHorseConfig

class Configuration(ConfigurationSystem, ConfigurationSettings, ConfigurationHandlers, ConfigurationErrors):
    def __init__(self):
        config      = CrazyHorseConfig()
        self.initialize_application_settings(config)
        self.initialize_application_handlers(config)
        self.initialize_application_errors(config)
        self.process_orphaned_routes()
