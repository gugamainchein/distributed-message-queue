# Import app packages
import sys
import os
import json
import uuid
import requests
import logging
import colorlog
from dotenv import load_dotenv
from src.cognito_auth import handler as auth

load_dotenv()
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S'))
logger.addHandler(sh)


def handler(event=None, context=None):
    # Authenticate user
    logger.info('Calling Auth Function')
    jwt_response = auth()
    logger.info(f'Call made successfully! The return obtained was: {jwt_response}')

    # Formating variables
    headers = {'Authorization': jwt_response, 'MessageGroupId': str(uuid.uuid4())}
    body = json.dumps({'message': 'Message testing'})
    api_url = os.environ.get('API_URL')

    # Structure API request to send message to Queue
    logger.info('Calling Message Route')
    queue_response = requests.post(api_url, data=body, headers=headers)
    queue_response = queue_response.json()['SendMessageResponse']['SendMessageResult']['MessageId']
    logger.info(f'Call made successfully! The return obtained was: {queue_response}')

    return {
        'statusCode': 200,
        'body': queue_response
    }


if __name__ == '__main__':
    print(handler())