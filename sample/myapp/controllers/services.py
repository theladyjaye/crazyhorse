import http.client 
from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.results import JsonResult
from crazyhorse.web.decorators import route

class NewsController(CrazyHorseController):

    @route(name        = "service_twitter",
           path        = "/services/twitter")
    def twitter(self):
        twitter = http.client.HTTPConnection("api.twitter.com")
        twitter.request("GET", "/1/statuses/user_timeline.json?screen_name=logix812")
        timeline = twitter.getresponse()
        json = timeline.read()
        twitter.close()

        return self.json(json, encode=False)