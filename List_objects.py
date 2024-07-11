import boto3

# Initializing the S3 client
s3 = boto3.client('s3')

# Listing the Buckets
response = s3.list_objects_v2(Bucket="dewayne-boto3-06212024")

# Printing the folders in the content  
for content in response["Contents"]:
    
    # Adding an if statement since there are multiple files and we just want the text file. Adding the -4 will be the last for characters so you can find the file type
    if(".txt" in content["Key"][-4:]):
    
        # Printing the content
        print (content["Key"])