from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.decorators import route
from crazyhorse.web.decorators import route_method

class AboutController(CrazyHorseController):

    @route(name        = "about_index",
           path        = "/about")
    def index(self):
        model = {"message":"about"}
        return self.view("about", model)


    @route(name        = "AboutFoo",
           path        = "/about/{item}/{action}",
           constraints = {"item":r"\d+", "action":r"read|archive"})
    def foo(self, item, action):
        model = {"message":"It Works! (foo)", "item":item, "action":action}
        return self.view("about_foo", model)

    @route_method("POST","AboutFoo")
    def foo_post(self, item, action):
        model = {"message":"It Works! (foo_post)"}
        return self.view("about_foo_post", model)

    @route_method("PUT","AboutFoo")
    def foo_put(self, item, action):
        model = {"message":"It Works! (foo_put)"}
        return self.view("about_foo_put", model)

    @route_method("POST","Blueberries!")
    def fooberries(self, item, action):
        pass
