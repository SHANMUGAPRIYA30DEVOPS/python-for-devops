#using boto3 - install aws cli, boto3, aws configure
# aws boto3 official documentation  - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='my-priya-new-bucket'  
)

print(response)
