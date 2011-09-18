from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.actions import route
from crazyhorse.web.actions import route_method

class DashboardController(CrazyHorseController):

    @route(name        = "DashboardMain",
           path        = "/admin")
    def foo(self):
        model = {"message":"It Works! (foo)"}
        return self.view("about_foo", model)
