import json
import boto3
import os
from datetime import *


def send_email(instance_id):
    print(instance_id)
    RECIPIENT_MAIL = json.loads(os.environ['destination_email'])
    SENDER_EMAIL = json.loads(os.environ['source_email'])
    AWS_REGION = "ap-south-1"
    SUBJECT = "GPU Instance is running for more than 5 hours"
    BODY_TEXT = (
        "GPU Instance Long Running Alert\r\n"
        "GPU Instance with instance id as {{ instance_id }} in Singapore is running for more than 5 hours.")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Instance ID: """ + str(instance_id) + """</h1>
      <p>GPU Instance with instance id as """ + str(instance_id) + """ in Singapore region is running for more than 5 hours.</p>
    </body>
    </html>
                """
    CHARSET = "UTF-8"
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': RECIPIENT_MAIL,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER_EMAIL,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-type',
                'Values': [
                    'p3.2xlarge'
                ]
            },
        ]
    )
    for reservations in (response["Reservations"]):
        for instance in (reservations["Instances"]):
            timenow = datetime.now()
            launchtime = instance["LaunchTime"].replace(tzinfo=None)
            diff = timenow - launchtime
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            instance_id = instance["InstanceId"]
            if (hours > 5):
                send_email(instance_id)
            print(hours)
