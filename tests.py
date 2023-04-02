import unittest
import requests

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000/calculate'

    def test_addition(self):
        data = {'a': 2, 'b': 3, 'operator': '+'}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 5)

    def test_subtraction(self):
        data = {'a': 5, 'b': 3, 'operator': '-'}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2)

    def test_multiplication(self):
        data = {'a': 2, 'b': 3, 'operator': '*'}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 6)

    def test_division(self):
        data = {'a': 6, 'b': 3, 'operator': '/'}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2)

if __name__ == '__main__':
    unittest.main()
