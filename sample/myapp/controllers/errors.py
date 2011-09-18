from crazyhorse.web.controller import CrazyHorseController
class ServerErrorController(CrazyHorseController):

    def error_404(self):
        model = {"message":"We could not find what you were looking for"}
        return self.view("404", model)

    def error_500(self):
        model = {"message":"There was an error"}
        return self.view("500", model)