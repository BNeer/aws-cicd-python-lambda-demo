import unittest
from src.lambda_function.app import handler

class TestLambdaFunction(unittest.TestCase):
    def test_handler(self):
        event = {}  # Mock event data
        context = {}  # Mock context data
        response = handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('body', response)

if __name__ == '__main__':
    unittest.main()