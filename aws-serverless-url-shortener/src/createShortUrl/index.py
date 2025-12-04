import json

def lambda_handler(event, context):
    # Determine if 'body' exists (proxy integration) or use event directly (non-proxy)
    if 'body' in event:
        # Proxy integration: body is a JSON string
        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON in body"})
            }
    else:
        # Non-proxy integration: event is already a dict
        body = event

    # Get the URL from the body
    url = body.get('url')
    if not url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'url' parameter"})
        }

    # TODO: Replace this with actual URL shortening logic
    short_url = "abc123"

    # Return response (always as JSON string)
    return {
        "statusCode": 200,
        "body": json.dumps({"short_url": short_url})
    }
