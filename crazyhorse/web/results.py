import json
from crazyhorse.web.response import ResponseStatus

class CrazyHorseResult:

    def __init__(self, *args, **kwargs):
        self._httpcontext = None
    
    @property
    def httpcontext(self):
        return self._httpcontext
    
    @property
    def content_type(self):
        return "text/plain"

class JsonResult(CrazyHorseResult):

    def __init__(self, data, encode=True):
        self._encode = encode
        self.data = data
    
    @property
    def content_type(self):
        return "application/json"

    def __call__(self):
        
        if self._encode:
            return json.dumps(self.data)
        else:
            return self.data

class RedirectResult(CrazyHorseResult):

    def __init__(self, url):
        self.url = url

    def __call__(self):
        response = self.httpcontext.response
        response.headers.add("Location", self.url)
        response.status = ResponseStatus.MOVED_TEMPORARILY
        return None

class NotFoundResult(CrazyHorseResult):

    def __call__(self):
        response = self.httpcontext.response
        response.status = ResponseStatus.NOT_FOUND
        return None

class ServerErrorResult(CrazyHorseResult):

    def __call__(self):
        response = self.httpcontext.response
        response.status = ResponseStatus.SERVER_ERROR
        return None

class ForbiddenResult(CrazyHorseResult):

    def __call__(self):
        response = self.httpcontext.response
        response.status = ResponseStatus.FORBIDDEN
        return None