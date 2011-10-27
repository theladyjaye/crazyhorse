from crazyhorse.security.authorization import CrazyHorseAuthorizationProvider

class DefaultAuthorizationProvider(CrazyHorseAuthorizationProvider):

    def is_authorized(self, httpcontext):
        status = httpcontext.request.headers["X-CrazyHorse-Authorization"]
        return status


class OtherAuthorizationProvider(CrazyHorseAuthorizationProvider):

    def is_authorized(self, httpcontext):
        status = httpcontext.request.headers["X-CrazyHorse-Authorization"]
        return status
