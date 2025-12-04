import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlTable')

def lambda_handler(event, context):
    short_id = event['pathParameters']['id']

    resp = table.get_item(Key={'id': short_id})
    item = resp.get('Item')

    if not item:
        return {'statusCode': 404, 'body': 'Not found'}

    # update click counter
    table.update_item(
        Key={'id': short_id},
        UpdateExpression='SET clicks = clicks + :inc',
        ExpressionAttributeValues={':inc': 1}
    )

    return {
        "statusCode": 302,
        "headers": {"Location": item['long_url']},
        "body": ""
    }

