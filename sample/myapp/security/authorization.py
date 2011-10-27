from crazyhorse.security.authorization import CrazyHorseAuthorizationProvider

class DefaultAuthorizationProvider(CrazyHorseAuthorizationProvider):

    def is_authorized(self, httpcontext):
        return True


class OtherAuthorizationProvider(CrazyHorseAuthorizationProvider):

    def is_authorized(self, httpcontext):
        return True
