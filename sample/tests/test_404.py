from test_base import TestCrazyHorseBase
import unittest

class TestCrazyHorse404(TestCrazyHorseBase):

    def test_404_get(self):
        #print("TestCrazyHorseRoutes: " + str(self))
        test_environ        = {"PATH_INFO": "/invalid_route",
                               "REQUEST_METHOD": "GET",
                               "HTTP_USER_AGENT": "Unknown",
                               "HTTP_ACCEPT":"text/html",
                               "HTTP_ACCEPT_LANGUAGE":"en-US",
                               "HTTP_ACCEPT_CHARSET":"utf-8",
                               "REMOTE_ADDR":"127.0.0.1"}
        test_start_response = lambda x,y: x
        self.application(test_environ, test_start_response)
        self.assertTrue(True)

    def test_404_post(self):
        test_environ        = {"PATH_INFO": "/invalid_route",
                               "REQUEST_METHOD": "POST",
                               "HTTP_USER_AGENT": "Unknown",
                               "HTTP_ACCEPT":"text/html",
                               "HTTP_ACCEPT_LANGUAGE":"en-US",
                               "HTTP_ACCEPT_CHARSET":"utf-8",
                               "REMOTE_ADDR":"127.0.0.1"}
        test_start_response = lambda x,y: x
        self.application(test_environ, test_start_response)
        self.assertTrue(True)
#
    #def test_404_put(self):
    #    test_environ        = {"PATH_INFO": "/invalid_route",
    #                           "REQUEST_METHOD": "PUT",
    #                           "HTTP_USER_AGENT": "Unknown",
    #                           "HTTP_ACCEPT":"text/html",
    #                           "HTTP_ACCEPT_LANGUAGE":"en-US",
    #                           "HTTP_ACCEPT_CHARSET":"utf-8",
    #                           "REMOTE_ADDR":"127.0.0.1"}
    #    test_start_response = lambda x,y: x
    #    self.application(test_environ, test_start_response)
    #    self.assertTrue(True)
#
    #def test_404_delete(self):
    #    test_environ        = {"PATH_INFO": "/invalid_route",
    #                           "REQUEST_METHOD": "DELETE",
    #                           "HTTP_USER_AGENT": "Unknown",
    #                           "HTTP_ACCEPT":"text/html",
    #                           "HTTP_ACCEPT_LANGUAGE":"en-US",
    #                           "HTTP_ACCEPT_CHARSET":"utf-8",
    #                           "REMOTE_ADDR":"127.0.0.1"}
    #    test_start_response = lambda x,y: x
    #    self.application(test_environ, test_start_response)
    #    self.assertTrue(True)
#
    #def test_404_odd_method(self):
    #    test_environ        = {"PATH_INFO": "/invalid_route",
    #                           "REQUEST_METHOD": "STRANGE",
    #                           "HTTP_USER_AGENT": "Unknown",
    #                           "HTTP_ACCEPT":"text/html",
    #                           "HTTP_ACCEPT_LANGUAGE":"en-US",
    #                           "HTTP_ACCEPT_CHARSET":"utf-8",
    #                           "REMOTE_ADDR":"127.0.0.1"}
    #    test_start_response = lambda x,y: x
    #    self.application(test_environ, test_start_response)
    #    self.assertTrue(True)