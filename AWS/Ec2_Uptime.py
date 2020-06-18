import json
import boto3
from datetime import *
from decimal import *

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-type',
            'Values': [
                'm5.large'
            ]
        },
    ]
)
#.get(
#    'Reservations', []
#    )
#print(reservations[0]["Instances"][0]["LaunchTime"])
for reservations in (response["Reservations"]):
    for instance in (reservations["Instances"]):
        print(instance["LaunchTime"])
timenow = datetime.now()
print(timenow)
#def lambda_handler(event, context):
#    apigateway = boto3.client('apigateway')
#    usage_plans_raw_data=apigateway.get_usage_plans()['items']  # Capturing api respose from api gateway for getting usage plan data dynamically
#    usage_plan=[]
#    for usage_plan_id in usage_plans_raw_data:
#        x=usage_plan_id['id']
#        usage_plan.append(x)
#        print(usage_plan)
