import unittest
import os
from app import app


class BasicTestCase(unittest.TestCase):
    
    def test_index(self):
        """Route Testing"""
        test1 = app.test_client(self)
        response = test1.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_challenge(self):
        """Route Testing"""
        test2 = app.test_client(self)
        response = test2.get('/challenge', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_scoreboard(self):
        """Route Testing"""
        test3 = app.test_client(self)
        response = test3.get('/scoreboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()