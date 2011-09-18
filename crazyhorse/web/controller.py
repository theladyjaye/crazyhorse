from crazyhorse.web.results import Redirect

class CrazyHorseController(object):
    view_class = None

    def __init__(self):
        self._current_context = None

    def initialize(self, request):
        pass

    @property
    def current_context(self):
        return self._current_context

    def redirect(self, location):
        return Redirect(location)

    def view(self, *args, **kwargs):
        return CrazyHorseController.view_class(*args, **kwargs)
