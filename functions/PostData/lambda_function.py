import boto3


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        test = dynamodb.Table('test')
        result = test.put_item(
            Item={
                "fullname": event.get("fullname"),
                "address": event.get("address"),
                "age": event.get("age")
            }
        )
        return {
            "status": "OK"
        }
    except Exception as e:
        status = {
            "error": True,
            "message": "Not found data"
        }
        return status
