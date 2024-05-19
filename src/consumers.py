# Import app modules
import json


def handler(event, context=None):
    # Return the message received from the SQS
    queue_message = json.loads(event['Records'][0]['body'])

    return {
        'statusCode': 200,
        'body': json.dumps(queue_message)
    }


if __name__ == '__main__':
    print(handler({
        'Records':[{
            'body': '{"message": "testing consumer!"}',
        }]
    }))
