import boto3

# Initializing the S3 client
s3 = boto3.client('s3')

# Listing the Buckets
response = s3.list_objects_v2(Bucket="dewayne-boto3-06212024")

extension = ".txt"

# Printing the folders in the content  
for content in response["Contents"]:
    
    # Adding an if statement since there are multiple files and we just want the text file then adding the -len with exension file
    if(extension in content ["Key"][-(len(extension)):]):
    
        # Printing the content
        print (content["Key"])