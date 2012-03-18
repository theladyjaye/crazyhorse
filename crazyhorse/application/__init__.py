from itertools import repeat
from itertools import imap
from itertools import ifilter

class CrazyHorseExecutionContext(object):
    def __init__(self, application, features, httpcontext, controller_factory):
        self.application        = application
        self.httpcontext        = httpcontext
        self.controller_factory = controller_factory
        self.features           = imap(lambda feature,ctx: feature(ctx), features, repeat(httpcontext))
    
    def __enter__(self):
        context = self.httpcontext
        features = self.features
        self.application.application_begin_request(context)
        
        try:
            features.authenticate(context)
        except AttributeError:
            pass

        # if you would like __crazyhorse_exit__ to be called on a feature when the 
        # context manager exits, your call on the feature must return an object
        # that has the method __crazyhorse_exit__
        self.features = list(ifilter(None, features))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.application.application_end_request(self.httpcontext)
        #map(lambda x: x.__crazyhorse_exit__(), self.features)
        [x.__crazyhorse_exit__() for x in self.features]