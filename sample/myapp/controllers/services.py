import httplib
from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.results import SimpleJsonResult
from crazyhorse.web.actions import route

class NewsController(CrazyHorseController):

    @route(name        = "service_twitter",
           path        = "/services/twitter")
    def twitter(self):
        twitter = httplib.HTTPConnection("api.twitter.com")
        twitter.request("GET", "/1/statuses/user_timeline.json?screen_name=logix812")
        timeline = twitter.getresponse()
        json = timeline.read()
        twitter.close()

        return SimpleJsonResult(json)
