import json, uuid, boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body['url']

    short_id = str(uuid.uuid4())[:8]  # simple short ID

    table.put_item(Item={
        'id': short_id,
        'long_url': long_url,
        'clicks': 0
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'id': short_id
        })
    }
