import crazyhorse
from crazyhorse.web.application import CrazyHorseApplication

class MyApp(CrazyHorseApplication):
  def application_start(self):
    crazyhorse.get_logger().debug("application_start")