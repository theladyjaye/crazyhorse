import unittest
from crazyhorse.application import wsgi
from myapp.application import MyApp
from tests.test_base import TestCrazyHorseBase
#from tests.test_routes import TestCrazyHorseRoutes
#from tests.test_404 import TestCrazyHorse404
from tests.test_config import TestCrazyHorseConfig
from tests.test_get_routes import TestCrazyHorseGetRoutes

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCrazyHorseConfig))
    suite.addTest(unittest.makeSuite(TestCrazyHorseGetRoutes))
    #suite.addTest(unittest.makeSuite(TestCrazyHorseRoutes))
    #suite.addTest(unittest.makeSuite(TestCrazyHorse404))
    return suite

if __name__ == "__main__":
    TestCrazyHorseBase.app = wsgi.Application(MyApp())
    unittest.TextTestRunner(verbosity=2).run(suite())