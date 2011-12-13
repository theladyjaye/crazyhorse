class CrazyHorseExecutionContext:
    def __init__(self, application, features, httpcontext):
        self.application = application
        self.httpcontext = httpcontext
        self.features = features
    
    def __enter__(self):
        context = self.httpcontext
        self.application.begin_request(context)
        self.features = [y for x in self.features for y in (x(context),) if y is not None]
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.application.end_request(self.httpcontext)
        (x.__crazyhorse_exit__() for x in self.features)