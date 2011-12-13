import unittest
import os
from tests.test_base import TestCrazyHorseBase
from tests.context import TestContext
from crazyhorse.configuration.manager import Configuration

class TestCrazyHorseAuthorizationRoutes(TestCrazyHorseBase):

    def test_home_auth_default_pass(self):
        context  = TestContext.default_context()
      
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/authorize_default"
        context["HTTP_X_CRAZYHORSE_AUTHORIZATION"] =  True
      
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result

        self.assertEqual("authorize_default_success", result.model["message"])
    
    def test_home_auth_default_fail(self):
        context  = TestContext.default_context()
      
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/authorize_default"
        context["HTTP_X_CRAZYHORSE_AUTHORIZATION"] =  False
      
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result

        self.assertEqual("authorize_default_failure", result.model["message"])
    
    def test_home_auth_other_pass(self):
        context  = TestContext.default_context()
      
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/authorize_other"
        context["HTTP_X_CRAZYHORSE_AUTHORIZATION"] =  True
      
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result

        self.assertEqual("authorize_other_success", result.model["message"])
    
    def test_home_auth_other_fail(self):
        context  = TestContext.default_context()
      
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/authorize_other"
        context["HTTP_X_CRAZYHORSE_AUTHORIZATION"] =  False
      
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result

        self.assertEqual("authorize_other_failure", result.model["message"])