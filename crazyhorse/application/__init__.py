class CrazyHorseExecutionContext(object):
    def __init__(self, application, features, httpcontext, controller_factory):
        self.application        = application
        self.httpcontext        = httpcontext
        self.controller_factory = controller_factory
        self.features           = features
    
    def __enter__(self):
        context = self.httpcontext
        self.application.application_begin_request(context)
        self.features = [y for x in self.features for y in (x(context),) if y is not None]
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.application.application_end_request(self.httpcontext)
        (x.__crazyhorse_exit__() for x in self.features)