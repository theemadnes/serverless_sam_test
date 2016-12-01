from __future__ import print_function
import datetime
import json
import boto3
import os
import urllib

# set up client connection to DynamoDB outside of lambda_handler using environment variables
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

# this is demo, so we'll hardcode the customerId to 'client1', which is used as the hash key
customer_id = 'client1'

def lambda_handler(event, context):
    # index metadata to dynamoDB
    print('Putting item to DynamoDB')
    table.put_item(
        Item = {
            'customerId': customer_id,
            'isoTimestamp': datetime.datetime.utcnow().isoformat(),
            'objectKey': urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
            }
        )
    return "Done."
