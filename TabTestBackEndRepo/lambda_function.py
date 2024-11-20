import json

def lambda_handler(event, context):
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))
    
    # Some commen t
    # Create a response object
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from my Lambda version 03!",
            # "input": event
        })
    }
    
    # Return the response
    return response
