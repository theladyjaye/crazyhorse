import unittest
import os
from test_base import TestCrazyHorseBase
from context import TestContext
from crazyhorse.configuration.manager import Configuration

class TestCrazyHorseGetRoutes(TestCrazyHorseBase):

    def test_index(self):

      context  = TestContext.default_context()
      
      context["REQUEST_METHOD"] = "GET"
      context["PATH_INFO"]      = "/"
      
      http_context = self.application(context, TestContext.default_response())
      result =  http_context.response.result
      
      self.assertEqual(Configuration.APP_SETTINGS["twitterApiKey"], result.model["twitterApiKey"])
      self.assertEqual(Configuration.APP_SETTINGS["newsPhotosPath"], result.model["newsPhotosPath"])
      self.assertEqual(Configuration.CUSTOM_FOO_SECTION.lucy, result.model["custom_lucy"])
      self.assertEqual(Configuration.CUSTOM_FOO_SECTION.tail, result.model["custom_tail"])

    def test_about_index(self):

        context  = TestContext.default_context()
        
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/about"
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual("about", result.model["message"])

    def test_contact_index(self):

        context  = TestContext.default_context()
        
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/contact"
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual("contact", result.model["message"])
      
    def test_news_index(self):

        context  = TestContext.default_context()
        
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/news"
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual("news", result.model["message"])

    def test_news_category_latest(self):
        category = "latest"
        context  = TestContext.default_context()
        
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/news/" + category
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual(category, result.model["category"])
        self.assertEqual("category", result.model["type"])
    
    
    def test_news_category_featured(self):
        category = "featured"
        context  = TestContext.default_context()
              
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/news/" + category
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual(category, result.model["category"])
        self.assertEqual("category", result.model["type"])

    
    def test_news_category_unknown(self):
        category = "foo"
        context  = TestContext.default_context()
        context["REQUEST_METHOD"] = "GET"
        context["PATH_INFO"]      = "/news/" + category
        
        http_context = self.application(context, TestContext.default_response())
        result =  http_context.response.result
        
        self.assertEqual(category, result.model["category"])
        self.assertEqual("catchall", result.model["type"])
