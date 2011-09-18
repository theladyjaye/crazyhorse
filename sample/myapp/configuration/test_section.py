from crazyhorse.configuration.sections import ConfigurationSection
class TestSection(ConfigurationSection):

    def __init__(self):
        self.lucy = None
        self.tail = None

    def __call__(self, section):
        
        self.lucy = section["lucy"] + " - Yes she is"
        self.tail = section["tail"] + " - All the time"
        return self
