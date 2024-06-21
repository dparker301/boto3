import boto3

# Creating a S3 bucket
s3 = boto3.client('s3')

response = s3.create_bucket(
    
    Bucket='dewayne-boto3-06212024'

)
#
print(response)