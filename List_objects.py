import boto3

# Initializing the S3 client
s3 = boto3.client('s3')

# Listing the Buckets
response = s3.list_objects_v2(Bucket="dewayne-boto3-06212024")

#print(response)

# Printing the folders in the content  
for content in response["Contents"]:
    
    # Adding an if statement since there are multiple files and we just want the text file
    if(".txt" in content["Key"]):
    
        # Printing the content
        print (content["Key"])