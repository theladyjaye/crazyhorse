import unittest
import os
from test_base import TestCrazyHorseBase
from context import TestContext
from crazyhorse.configuration.manager import Configuration

class TestCrazyHorseAuthorizationRoutes(TestCrazyHorseBase):

    def test_home_auth_test(self):
        context  = TestContext.default_context()
      
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/authorize"
      
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual("authorize", result.model["message"])