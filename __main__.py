# Import app packages
import os
import json
import uuid
import requests
from dotenv import load_dotenv
from src.cognito_auth import handler as auth

load_dotenv()


def handler(event=None, context=None):
    # Authenticate user
    jwt_response = auth()

    # Formating variables
    headers = {'Authorization': jwt_response, 'MessageGroupId': str(uuid.uuid4())}
    body = json.dumps({'message': 'Message testing'})
    api_url = os.environ.get('API_URL')

    # Structure API request to send message to Queue
    queue_response = requests.post(api_url, data=body, headers=headers)
    queue_response = queue_response.json()['SendMessageResponse']['SendMessageResult']['MessageId']

    return {
        'statusCode': 200,
        'body': queue_response
    }


if __name__ == '__main__':
    print(handler())