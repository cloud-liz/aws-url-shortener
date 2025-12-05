import boto3
import os

# Connect to DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener')  # Make sure this matches your table name

def lambda_handler(event, context):
    # Safely get the path parameter
    path_params = event.get("pathParameters", {})
    short_id = path_params.get("id")  # This matches your API Gateway resource /{id}
    
    if not short_id:
        return {"statusCode": 400, "body": "Missing short ID in path"}

    # Fetch the item from DynamoDB
    try:
        resp = table.get_item(Key={'shortId': short_id})
    except Exception as e:
        return {"statusCode": 500, "body": f"DynamoDB error: {str(e)}"}

    item = resp.get('Item')
    if not item:
        return {"statusCode": 404, "body": "Short URL not found"}

    # Increment the click counter
    try:
        table.update_item(
            Key={'shortId': short_id},
            UpdateExpression='SET clicks = clicks + :inc',
            ExpressionAttributeValues={':inc': 1}
        )
    except Exception as e:
        # Log the error but still redirect
        print(f"Error updating clicks: {e}")

    # Redirect to the long URL
    return {
        "statusCode": 302,
        "headers": {"Location": item['longUrl']},
        "body": ""
    }


