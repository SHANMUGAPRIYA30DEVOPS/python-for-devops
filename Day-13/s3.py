#using boto3 - install aws cli, boto3, aws configure

import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='my-priya-new-bucket'  
)

print(response)
