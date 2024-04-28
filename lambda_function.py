import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda! This function has been deployed using Azure DevOps')
#     }
import logging
import numpy as np

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        operation = event.get('operation')
        numbers = event.get('numbers')

        if not operation or not numbers:
            raise ValueError("Operation and numbers are required")

        nums = [float(num) for num in numbers]

        if operation == 'add':
            result = np.sum(nums)
        elif operation == 'subtract':
            result = nums[0] - np.sum(nums[1:])
        elif operation == 'multiply':
            result = np.prod(nums)
        elif operation == 'divide':
            if 0 in nums[1:]:
                raise ValueError("Division by zero is not allowed")
            result = nums[0] / np.prod(nums[1:])
        else:
            raise ValueError("Unsupported operation")

        return {
            'statusCode': 200,
            'body': {
                'result': result
            }
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 400,
            'body': {
                'error': str(e)
            }
        }
