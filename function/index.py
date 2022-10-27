import json
from urllib import response
import boto3

s3_client = boto3.client('s3')


def func_handler(event, context):
    # TODO implement
    response = s3_client.list_buckets()
    print(response)

    return {
        'statusCode': 200,
        'body': "ok"
    }
