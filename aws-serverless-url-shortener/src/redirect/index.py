import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    short_id = event["pathParameters"]["shortId"]

    response = table.get_item(Key={"shortId": short_id})
    item = response.get("Item")

    if not item:
        return {"statusCode": 404, "body": "Not Found"}

    long_url = item["longUrl"]

    table.update_item(
        Key={"shortId": short_id},
        UpdateExpression="SET clicks = clicks + :val",
        ExpressionAttributeValues={":val": 1}
    )

    return {
        "statusCode": 301,
        "headers": {"Location": long_url}
    }

