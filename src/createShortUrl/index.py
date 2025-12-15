import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener') 

def lambda_handler(event, context):
    # Parse JSON body
    if 'body' in event:
        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            return {"statusCode": 400, "body": json.dumps({"error": "Invalid JSON in body"})}
    else:
        body = event

    url = body.get('url')
    if not url:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing 'url'"})}

    # Generate short ID
    short_id = str(uuid.uuid4())[:8]

    # Write to DynamoDB
    try:
        table.put_item(Item={
            "shortId": short_id,
            "longUrl": url,
            "clicks": 0
        })
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    # Return the short URL
    return {"statusCode": 200, "body": json.dumps({"short_url": short_id})}
