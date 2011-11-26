import json
from crazyhorse.web.response import ResponseStatus

class CrazyHorseResult(object):

    def __init__(self, *args, **kwargs):
        self._httpcontext = None
    
    @property
    def httpcontext(self):
        return self._httpcontext
    
    @property
    def content_type(self):
        return "text/plain"

class SimpleJsonResult(CrazyHorseResult):

    def __init__(self, json, encode=False):
        if encode:
            self.json = json.dumps(json)
        else:
            self.json = json
    
    @property
    def content_type(self):
        return "application/json"

    def __call__(self):
        
        return self.json

class Redirect(CrazyHorseResult):

    def __init__(self, location):
        self.location = location

    def __call__(self):
        response = self.httpcontext.response
        response.headers.add("Location", self.location)
        response.status = ResponseStatus.MOVED_TEMPORARILY
        return None