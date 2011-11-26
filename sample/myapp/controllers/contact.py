from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.decorators import route
from crazyhorse.web.decorators import route_method
from crazyhorse.utils import objectutils
from myapp.forms.contact import ContactForm

class ContactController(CrazyHorseController):

    @route(name        = "contact_index",
           path        = "/contact")
    def index(self):
        model = {"message":"contact"}
        return self.view("contact", model)
    
    @route_method("POST","contact_index")
    def submit(self):
        form   = ContactForm()

        params = self.httpcontext.request.data
        files  = self.httpcontext.request.files

        objectutils.map_form_dict(form, params)
        objectutils.map_form_dict(form, files)

        return self.view("contact", form.__dict__)
