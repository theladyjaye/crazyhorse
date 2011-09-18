import unittest
import os
from crazyhorse.application import wsgi

class TestCrazyHorseBase(unittest.TestCase):
    app = None

    def application(self, environ, start_response):
        TestCrazyHorseBase.app(environ, start_response)