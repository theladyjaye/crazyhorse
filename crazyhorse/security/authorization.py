class CrazyHorseAuthorizationProvider(object):
    def __init__(self, httpcontext):
        self._httpcontext = httpcontext

    @property
    def httpcontext(self):
        return self._httpcontext

    def is_authorized(self, httpcontext):
        return True