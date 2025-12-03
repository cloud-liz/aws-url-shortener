import json
import uuid
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    long_url = body.get("url")

    short_id = str(uuid.uuid4())[:8]

    table.put_item(Item={
        "shortId": short_id,
        "longUrl": long_url,
        "clicks": 0
    })

    return {
        "statusCode": 200,
        "body": json.dumps({"shortUrl": f"https://your-api/{short_id}"})
    }
