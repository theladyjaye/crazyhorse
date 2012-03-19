from crazyhorse.web.request import Request
from crazyhorse.web.response import Response

class HttpContext(object):

    CURRENT = None
    
    def __init__(self, environ, start_response):
        self.path           = environ["PATH_INFO"]
        self.method         = environ.get("REQUEST_METHOD", "GET").upper()
        self.request        = Request(environ)
        self.response       = Response()
        self.identity       = None

        # what is self.views used for?
        # self.views          = None

        self.session        = None
        self.environ        = environ
        self.start_response = start_response

        HttpContext.CURRENT = self
    
    def __iter__(self):
        return iter(self.response(self))