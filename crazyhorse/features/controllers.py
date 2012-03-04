from crazyhorse.utils.tools import import_class

class CrazyhorseControllerFactory(object):
    
    def __init__(self):
        self.registry = {}

    def create_controller(self, httpcontext, name):
        if name not in self.registry:
            cls = import_class(name)
            self.registry[name] = cls
        else:
            cls = self.registry[name]

        return cls()