import json
import boto3
from datetime import *
from decimal import *

#*********************************************************** Fetch data from API Gateway for each Usage Plan ID***************************************************
def lambda_handler(event, context):
    apigateway = boto3.client('apigateway')
    usage_plans_raw_data=apigateway.get_usage_plans()['items']  # Capturing api respose from api gateway for getting usage plan data dynamically
    usage_plan=[]
    for usage_plan_id in usage_plans_raw_data:
        x=usage_plan_id['id']
        usage_plan.append(x)
        print(usage_plan)