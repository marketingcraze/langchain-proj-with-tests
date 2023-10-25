import unittest
from flask import Flask, jsonify
from app import app
import requests

# unit tests for the flask app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def testSuccessfulConnection(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.data)
        self.assertEqual(response['status'], 'success')

    def testBadConnection(self):
        invalidData = 'non-jsonifyable-object'
        response = self.app.post('/', data=invalidData)
        self.assertEqual(response.status_code, 400)
        response = json.loads(response.data)
        self.assertEqual(response['status'], 'error')


if __name__ == '__main__':
    unittest.main()