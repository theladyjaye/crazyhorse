from crazyhorse.web.results import Redirect
from crazyhorse.web.results import JsonResult

class CrazyHorseController(object):
    view_class = None

    def __init__(self):
        self._httpcontext = None

    def initialize(self, request):
        pass

    @property
    def httpcontext(self):
        return self._httpcontext

    def redirect(self, location):
        return Redirect(location)

    def json(self, data):
        """Where data is a dict"""
        return JsonResult(data)


    def view(self, *args, **kwargs):
        return CrazyHorseController.view_class(*args, **kwargs)
