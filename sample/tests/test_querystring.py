import unittest
import os
from test_base import TestCrazyHorseBase
from context import TestContext
from crazyhorse.configuration.manager import Configuration

class TestCrazyHorseQueryStringFeature(TestCrazyHorseBase):

    def test_querystring_simple(self):

      context  = TestContext.default_context()
      
      context["REQUEST_METHOD"] = "GET"
      context["PATH_INFO"]      = "/"
      context["QUERY_STRING"]   = "&id=12&lucy=dog&ollie=cat"
      
      http_context = self.application(context, TestContext.default_response())
      querystring =  http_context.request.querystring
      
      self.assertEqual(12, int(querystring["id"]))
      self.assertEqual("dog", querystring["lucy"])
      self.assertEqual("cat", querystring["ollie"])
    
    def test_querystring_array(self):

      context  = TestContext.default_context()
      
      context["REQUEST_METHOD"] = "GET"
      context["PATH_INFO"]      = "/"
      context["QUERY_STRING"]   = "&id=12&dog=lucy&dog=tucker&dog=dexter&cat=ollie"
      
      http_context = self.application(context, TestContext.default_response())
      querystring =  http_context.request.querystring
      
      self.assertEqual(12, int(querystring["id"]))
      self.assertEqual(3, len(querystring["dog"]))
      self.assertEqual("lucy", querystring["dog"][0])
      self.assertEqual("tucker", querystring["dog"][1])
      self.assertEqual("dexter", querystring["dog"][2])
      self.assertEqual("ollie", querystring["cat"])