import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_addition(self):
        event = {'operation': 'add', 'numbers': [3, 5, 7]}
        expected_result = 15
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body']['result'], expected_result)

    def test_subtraction(self):
        event = {'operation': 'subtract', 'numbers': [10, 2, 3]}
        expected_result = 5
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body']['result'], expected_result)

    def test_multiplication(self):
        event = {'operation': 'multiply', 'numbers': [2, 3, 4]}
        expected_result = 24
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body']['result'], expected_result)

    def test_division(self):
        event = {'operation': 'divide', 'numbers': [100, 2, 5]}
        expected_result = 10
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body']['result'], expected_result)

    def test_division_by_zero(self):
        event = {'operation': 'divide', 'numbers': [100, 0, 5]}
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)
        self.assertIn('error', result['body'])

    def test_unsupported_operation(self):
        event = {'operation': 'power', 'numbers': [2, 3]}
        result = lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)
        self.assertIn('error', result['body'])

if __name__ == '__main__':
    unittest.main()
