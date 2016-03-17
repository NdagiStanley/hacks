import unittest

from flask_app import app


class AppTestCase(unittest.TestCase):
    """
    AppTestCase
    """

    def setUp(self):
        """Setting up the environment for testing"""
        print "=> Setting up the environment for testing"
        self.app = app.test_client()

    def tearDown(self):
        """Tearing down after tests"""
        print "=> Tearing down after tests"

    def test_api_index(self):
        """Test if the index page is working"""
        response = self.app.get('/')
        print '=> Getting to "/"'
        assert response.status == "200 OK"
        self.assertIn('Celery hack', response.data)

    def test_api_index(self):
        """Test if the celery requests page is working"""
        response = self.app.get('/celery_hack/1')
        print '=> Getting to "/celery_hack/<>"'
        assert response.status == "200 OK"
