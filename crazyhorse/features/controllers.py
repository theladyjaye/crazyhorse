from crazyhorse.utils.tools import import_class

class CrazyhorseControllerFactory(object):
    def __init__(self):
        self.registery = {}

    def create_controller(self, httpcontext, name):
        if name not in self.registry:
            cls = import_class(name)
            self.registery[name] = cls
        else:
            cls = self.registery[name]

        return cls()