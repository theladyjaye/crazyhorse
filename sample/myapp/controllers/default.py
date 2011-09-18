from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.actions import route
from crazyhorse.web.actions import route_method
class DefaultController(CrazyHorseController):

    @route(name        = "CatchAll",
           path        = "/nano")
    def index(self):
        print("CatchAll")
