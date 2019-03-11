import unittest
import requests
from pdb import set_trace
import json


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_fib_view_url1(self):
        response = requests.get('http://127.0.0.1:5000/fib/3/5')
        # set_trace()
        self.assertEqual(json.loads(response.content), [2, 3, 5])

    def test_fib_view_url2(self):
        response = requests.get('http://127.0.0.1:5000/fib/1/5')
        # set_trace()
        self.assertEqual(json.loads(response.content), [1, 1, 2, 3, 5])
        

    def test_fib_view_ur3(self):
        response = requests.get('http://127.0.0.1:5000/fib/5/3')
        # set_trace()
        self.assertEqual(json.loads(response.content), [2])
        

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()