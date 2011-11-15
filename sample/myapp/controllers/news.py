from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.decorators import route

class NewsController(CrazyHorseController):

    @route(name        = "news_index",
           path        = "/news")
    def index(self):
        model = {"message":"news"}
        return self.view("news", model)
    

    @route(name        = "news_category",
           path        = "/news/{category}",
           constraints = {"category":r"latest|featured"})
    def news_category(self, category):
        model = {"message":"news", "category":category, "type":"category"}
        return self.view("news_category", model)
      
    
    @route(name        = "news_catchall",
           path        = "/news/{category}")
    def news_catachall(self, category):
        model = {"message":"news - catchall", "category":category, "type":"catchall"}
        return self.view("news_category", model)
