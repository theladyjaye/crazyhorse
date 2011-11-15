from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.configuration.manager import Configuration
from crazyhorse.web.decorators import route
from crazyhorse.web.decorators import authorize

class HomeController(CrazyHorseController):
    
    @route(name = "Home", path = "/")
    def index(self):
        model = {"message":"home", "dog":"Unknown", "cat":"Unknown"}
        request = self.current_context.request
        
        if request.querystring is not None:
            for key in request.querystring:
                model[key] = request.querystring[key]
        
        model["twitterApiKey"]  = Configuration.APP_SETTINGS["twitterApiKey"]
        model["newsPhotosPath"] = Configuration.APP_SETTINGS["newsPhotosPath"]

        model["custom_lucy"]  = Configuration.CUSTOM_FOO_SECTION.lucy
        model["custom_tail"] = Configuration.CUSTOM_FOO_SECTION.tail

        return self.view("home", model)

    @authorize
    @route(name = "TestAuthDefault", path = "/authorize_default")
    def auth_test_default(self):
        model = {"message":"authorize_default_success"}
        request = self.current_context.request

        return self.view("home", model)
    
    @authorize("other")
    @route(name = "TestAuthOther", path = "/authorize_other")
    def auth_test_other(self):
        model = {"message":"authorize_other_success"}
        request = self.current_context.request

        return self.view("home", model)
