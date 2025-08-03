import unittest
import json
from app import app

class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_1_create_user(self):
        response = self.client.post('/users', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "testpass123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"User created", response.data)

    def test_2_login_success(self):
        response = self.client.post('/login', json={
            "email": "testuser@example.com",
            "password": "testpass123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"success", response.data)

    def test_3_login_failure(self):
        response = self.client.post('/login', json={
            "email": "wrong@example.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"failed", response.data)

    def test_4_search_user(self):
        response = self.client.get('/search?name=Test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test User", response.data)

    def test_5_get_all_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"testuser@example.com", response.data)

if __name__ == '__main__':
    unittest.main()
