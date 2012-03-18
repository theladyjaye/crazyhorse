from crazyhorse.web.headers import Headers
class Request(object):

    def __init__(self, environ):

        # self.environment    = environ
        #self.path           = environ["PATH_INFO"]
        #self.request_method = environ.get("REQUEST_METHOD", "GET").upper()
        #self.user_agent     = environ.get("HTTP_USER_AGENT", "Unknown")
        #self.accepts        = environ.get("HTTP_ACCEPT", "text/plain")
        #self.language       = environ.get("HTTP_ACCEPT_LANGUAGE", "en-US")
        #self.charset        = environ.get("HTTP_ACCEPT_CHARSET", "utf-8")
        #self.remote_address = environ.get("REMOTE_ADDR", "0.0.0.0")

        self.querystring    = None
        self.cookies        = None
        self.data           = None
        self.files          = None

        http_filter            = (x for x in environ if x.startswith("HTTP"))
        http_header_key_values = ((x[5:].replace("_", "-").lower(), environ[x]) for x in http_filter)
        self.headers           = Headers.with_collection(http_header_key_values)

    @property
    def is_ajax_request(self):
        
        try:
            ajax_header = self.headers["x-requested-with"].lower()
        except AttributeError:
            return False
        
        if ajax_header == "xmlhttprequest":
            return True
        
        return False
