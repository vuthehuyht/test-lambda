import boto3


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        test = dynamodb.Table('test')
        result = test.get_item(
            Key={
                "fullname": event.get("fullname"),
                "address": event.get("address")
            }
        )
        return result.get("Item")
    except Exception as e:
        status = {
            "error": True,
            "message": "Not found data"
        }
        return status
