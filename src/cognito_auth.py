# Import app modules
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def handler():
    # Construct the Cognito token endpoint
    cognito_url_prefix = os.environ.get('COGNITO_URL_PREFIX')
    aws_region = os.environ.get('AWS_REGION')
    token_endpoint = f'https://{cognito_url_prefix}.auth.{aws_region}.amazoncognito.com/oauth2/token'

    # Construct the token payload
    token_payload = {
        'grant_type': 'client_credentials',
        'client_id': os.environ.get('COGNITO_CLIENT_ID'),
        'client_secret': os.environ.get('COGNITO_CLIENT_SECRET'),
        'scope': os.environ.get('COGNITO_CLIENT_SCOPE')
    }

    # Send the token request
    token_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    token_response = requests.post(token_endpoint, data=token_payload, headers=token_headers)
    token_response = token_response.json().get('access_token')

    return token_response


if __name__ == '__main__':
    print(handler())