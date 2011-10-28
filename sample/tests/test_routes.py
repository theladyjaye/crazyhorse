import unittest
import os
from test_base import TestCrazyHorseBase
from context import TestContext


class TestCrazyHorseRoutes(TestCrazyHorseBase):

    def test_multipart_form(self):

      context  = TestContext.default_context()
      filename = os.getcwd() + "/tests/input/data-multipart-form-data-chrome.txt"
      filesize = os.path.getsize(filename)
      body     = open(filename, "r")

      context["REQUEST_METHOD"] = "POST"
      context["PATH_INFO"]      = "/about/12345/read"
      context["wsgi.input"]     = body
      context["CONTENT_LENGTH"] = filesize
      context["CONTENT_TYPE"]   = "multipart/form-data; boundary=----WebKitFormBoundaryy68h9UzzE0zpkUU7"

      self.application(context, TestContext.default_response())
      self.assertTrue(True)

    def test_post(self):

      context  = TestContext.default_context()
      filename = os.getcwd() + "/tests/input/data-x-www-form-urlencoded.txt"
      filesize = os.path.getsize(filename)
      body     = open(filename, "r")

      context["REQUEST_METHOD"] = "POST"
      context["PATH_INFO"]      = "/about/12345/read"
      context["wsgi.input"]     = body
      context["CONTENT_LENGTH"] = filesize
      context["CONTENT_TYPE"] = "application/x-www-form-urlencoded"

      self.application(context, TestContext.default_response())
      self.assertTrue(True)

    def test_foo(self):
        #print("TestCrazyHorseRoutes: " + str(self))
        test_environ        = {"PATH_INFO": "/nano",
                               "REQUEST_METHOD": "GET",
                               "HTTP_USER_AGENT": "Unknown",
                               "HTTP_ACCEPT":"text/html",
                               'QUERY_STRING': '&id=12&lucy=dog',
                               "HTTP_ACCEPT_LANGUAGE":"en-US",
                               "HTTP_ACCEPT_CHARSET":"utf-8",
                               "REMOTE_ADDR":"127.0.0.1"}

        self.application(test_environ, TestContext.default_response())
        self.assertTrue(True)