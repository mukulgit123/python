import json
import boto3
from datetime import *
from decimal import *

#*********************************************************** Fetch data from API Gateway for each Usage Plan ID***************************************************
def get_usage_plan():
    apigateway = boto3.client('apigateway')
    usage_plans_raw_data=apigateway.get_usage_plans()['items']  # Capturing api respose from api gateway for getting usage plan data dynamically
    usage_plan=[]
    for usage_plan_id in usage_plans_raw_data:
        x=usage_plan_id['id']
        usage_plan.append(x)
    return usage_plan
    
#********************************************** Call Api Gateway usage api for each usage plan ID************************************************

def apigateway(usage_plans):
    today = date.today() # - timedelta(1)          # Setting today's current date
    current_date=today.strftime('%Y-%m-%d')
    #print(current_date)
    apigateway = boto3.client('apigateway')
    current_year = today.year
    current_month = today.month
    #print(current_year)
    #print(current_month)
    print("calling from api_gateway function",usage_plans)  # List of usage plans to work on

    api_key_map={}
    for usage_id in usage_plans:
        #print(usage_id)
        response = apigateway.get_usage(usagePlanId=usage_id,startDate=current_date,endDate=current_date)
        quota = response['items']      # Monthly record of quota for each usage plan 
        print("Response for usage plan ID {} is {}".format(usage_id,quota))   #Response for each API usage plan ID
       
        quota_keys={}
        for key in quota.items():
            #print("key",key)
            api_key=key[0]
            max_quota=key[1][0][0]+key[1][0][1]
            print(max_quota)
            current_usage=key[1][0][0]
            print(current_usage)
            #current_usage123=key[1][-1][-1]
            #print(current_usage123)
            #print("quota remaining for {} in key {} is {} with max api quota {}".format(usage_id,api_key,current_usage,max_quota)) 
            quota_keys.update({api_key:(current_usage,max_quota)})
        api_key_map.update({usage_id:quota_keys}) 
    #print("\nApi key map\n",api_key_map)
    return api_key_map
    
#************************************************************Function For putting consolidated data into DyanmoDB********************************************************************
def put_dynamodb(api_key_map):
    #print(api_key_map)
    dynamodb = boto3.resource("dynamodb")
    date1 = datetime.today()
    cur_date = date1.strftime('%Y-%m-%d')
    api_gateway = boto3.client('apigateway')    # Api gateway boto3 client
    table = dynamodb.Table("api_gateway_quota_data")  # Dynamodb boto3 client
    data={}
    for key,value in api_key_map.items():
        usage_plan_id=key
        #print(key,value)
        usage_name = api_gateway.get_usage_plan(usagePlanId=usage_plan_id)['name']   # Usage Plan name from api gateway
        #print(usage_name)
        data.update({usage_name:{key:value}})
    #print(data)
    for usage_plan_name, api_key_data in data.items():
    #print(usage_plan_name,"and api key data is",api_key_data)
        for key,value in api_key_data.items():
            #print(key,value)
            for api_key,quota in value.items():
                #print(api_key,quota)
                getcontext().prec = 3
                percentage_consumtion= (Decimal(quota[0]/quota[1]))*100
                #print(percentage_consumtion)
                if (percentage_consumtion>0):  # Saving records where consumption is greater than 50% into DynamoDB
                    table.put_item(
                    Item = {
                    'usagePlanName': usage_plan_name,
                    'usagePlanId': key ,
                    'apiKeyId' : api_key,
                    'Current_Usage' : quota[0],
                    'Max_quota': quota[1],
                    'Percentage_consumtion': str(percentage_consumtion),
                    'Date': cur_date 
                        
                    })
            

#******************************************************************* Lambda event handler**********************************************************************

def lambda_handler(event, context):
    usage_plans=get_usage_plan()
    print("List of usage plans are",usage_plans)
    api_key_map=apigateway(usage_plans)
    print("lambda handler",api_key_map)
    put_dynamodb(api_key_map)

--------------------------------------------------------


import json
import boto3

client = boto3.client('apigateway')

def lambda_handler(event, context):

    response = client.get_usage(
        usagePlanId='srx0sb',
        keyId='r8md2fiwbl',
        startDate='2019-11-08',
        endDate='2019-11-18',
        limit=500
    )   
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    