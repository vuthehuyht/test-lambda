import boto3


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        test = dynamodb.Table('test')
        print("Got test table")
        result = test.update_item(
            Key={
                "fullname": event.get("fullname"),
                "address": event.get("address"),
            },
            UpdateExpression="set age=:age",
            ExpressionAttributeValues={
                ':age': event.get("age")
            },
            ReturnValues="UPDATED_NEW"
        )
        return {
            "status": "OK"
        }
    except Exception as e:
        status = {
            "error": True,
            "message": "Update false"
        }
        return status
