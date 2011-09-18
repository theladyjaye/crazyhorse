from crazyhorse.web.results import CrazyHorseResult
from jinja2 import Environment, PackageLoader, FileSystemLoader
#jinja2 = Environment(loader=PackageLoader('myapp', 'views'))
jinja2 = Environment(loader=FileSystemLoader(['/Users/dev/Projects/APP_CrazyHorse/sample/myapp/views']))


class Jinja2View(CrazyHorseResult):

    def __init__(self, name, model):
        self.model        = model;
        self.name         = name

    @property
    def content_type(self):
        return "text/html; charset=utf-8"

    def __call__(self):
        # can apply caching logic here if needed
        #response = self.context.response
        template = jinja2.get_template(self.name + ".html")

        # View Results should be responsible for setting the content type, not the controllers

        #response.headers.add("content-type", "text/html", charset="utf-8")
        try:
             template.render(self.model)
        except Exception as e:
            print(e.message)

        return template.render(self.model)#+ "<pre>{0}</pre>".format(str(self.context.environ))
