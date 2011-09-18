import unittest
from crazyhorse.application import wsgi
from myapp.application import MyApp
from tests.test_base import TestCrazyHorseBase
from tests.test_routes import TestCrazyHorseRoutes
from tests.test_404 import TestCrazyHorse404

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCrazyHorseRoutes))
    suite.addTest(unittest.makeSuite(TestCrazyHorse404))
    return suite

if __name__ == "__main__":
    TestCrazyHorseBase.app = wsgi.Application(MyApp())
    unittest.TextTestRunner(verbosity=2).run(suite())