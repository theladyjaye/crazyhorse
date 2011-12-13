import unittest
import os
from tests.test_base import TestCrazyHorseBase
from tests.context import TestContext
from crazyhorse.configuration.manager import Configuration
from myapp.security import authorization

class TestCrazyHorseConfig(TestCrazyHorseBase):

    def test_application_settings(self):
        self.assertEqual(Configuration.APP_SETTINGS["twitterApiKey"], "123456")
        self.assertEqual(Configuration.APP_SETTINGS["newsPhotosPath"], "/resources/managed/photos")
    
    def test_features(self):
        self.assertIsNotNone(Configuration.CRAZYHORSE_FEATURES["request_body"])
        self.assertIsNotNone(Configuration.CRAZYHORSE_FEATURES["querystrings"])
        self.assertIsNotNone(Configuration.CRAZYHORSE_FEATURES["cookies"])
        self.assertIsNotNone(Configuration.CRAZYHORSE_FEATURES["sessions"])

    def test_authorization_handlers(self):
        self.assertEqual(2, len(Configuration.APP_AUTHORIZATION_PROVIDERS))
        self.assertIsNotNone(Configuration.APP_AUTHORIZATION_PROVIDERS["default"])
        self.assertIsNotNone(Configuration.APP_AUTHORIZATION_PROVIDERS["other"])
        self.assertTrue(isinstance(Configuration.APP_AUTHORIZATION_PROVIDERS["default"], authorization.DefaultAuthorizationProvider))
        self.assertTrue(isinstance(Configuration.APP_AUTHORIZATION_PROVIDERS["other"], authorization.OtherAuthorizationProvider))
        
    def test_custom_section_exists(self):
        try:
            Configuration.CUSTOM_FOO_SECTION
            self.assertTrue(True)
        except AttributeError:
            self.fail("Custom section: CUSTOM_FOO_SECTION is not present")
    
    def test_custom_section_values(self):
        self.assertEqual(Configuration.CUSTOM_FOO_SECTION.lucy, "dog - Yes she is")
        self.assertEqual(Configuration.CUSTOM_FOO_SECTION.tail, "wag - All the time")
