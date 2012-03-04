from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.results import RedirectResult
from crazyhorse.web.results import JsonResult

class CrazyHorseController(object):
    view_class = None

    def initialize(self, request):
        pass

    @property
    def httpcontext(self):
        return HttpContext.CURRENT

    @property
    def request(self):
        return HttpContext.CURRENT.request

    @property
    def response(self):
        return HttpContext.CURRENT.response

    def redirect(self, location):
        return RedirectResult(location)

    def json(self, data):
        """Where data is a dict"""
        return JsonResult(data)


    def view(self, *args, **kwargs):
        return CrazyHorseController.view_class(*args, **kwargs)
