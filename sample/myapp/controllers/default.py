from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.decorators import route
from crazyhorse.web.decorators import route_method
class DefaultController(CrazyHorseController):

    @route(name        = "CatchAll",
           path        = "/nano")
    def index(self):
        print("CatchAll")
