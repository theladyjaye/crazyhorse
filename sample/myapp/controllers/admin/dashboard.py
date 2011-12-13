from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.decorators import route
from crazyhorse.web.decorators import route_method

class DashboardController(CrazyHorseController):

    @route(name        = "DashboardMain",
           path        = "/admin")
    def foo(self):
        model = {"message":"It Works! (foo)"}
        return self.view("about_foo", model)
