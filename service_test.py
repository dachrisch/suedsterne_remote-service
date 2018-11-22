# coding=utf-8
from unittest import TestCase

import jsonpickle

from service import remote_app


class TestRemotesApi(TestCase):
    def setUp(self):
        # creates a test client
        self.app = remote_app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_get_remote_methods(self):
        self.assertEqual(200, self.app.get('/remotes/api/v1.0/methods').status_code)

    def test_methods_as_json(self):
        response = self.app.get('/remotes/api/v1.0/methods').data
        methods = jsonpickle.decode(response)
        self.assertEqual(3, len(methods))
        self.assertIn('name', methods[0].keys())
        self.assertIn('remote', methods[0].keys())
        self.assertIn('login', methods[0].keys())
