import unittest
from app import create_app
from .test_setup import Setup

class TestFactory(Setup):
    def test_config(self):
        """Test create_app without passing test config."""

        self.assertFalse(create_app().testing)
        self.assertTrue(self.app.testing)
