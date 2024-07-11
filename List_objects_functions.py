import boto3

# Creating a function with no hard coded values
def filter_objects_extention(client, bucket, extension):
    keys = []
    # Creating a response
    response = client.list_objects_v2(Bucket=bucket)    
    # Now returning the keys
    for content in response["Contents"]:
        if(extension in content ["Key"][-(len(extension)):]):
            keys.append(content["Key"])
            
    # Returning the keys
    return keys

# Filtering the object extension
def list_objects_keys(client, bucket, prefix=""):
    keys = []
    # Creating a response
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)    
    # Now returning the keys
    for content in response["Contents"]:
        keys.append(content["Key"])
            
    # Returning the keys
    return keys
    
    
# Initializing the S3 client
s3 = boto3.client('s3')

response = list_objects_keys(s3, "dewayne-boto3-06212024", "folder/")
print(response)

# Listing the Buckets. Also can remove the ".txt" and add "/" to drill up
response = filter_objects_extention(s3, "dewayne-boto3-06212024", "/")
# Printing the content
print(response)