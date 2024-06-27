import boto3

# Imported the boto3 library and set up an S3 client. This client will allow me to interact with Amazon S3
s3 = boto3.client('s3')

# Use s3.put_object to upload it to the specified bucket.   
s3.put_object(Bucket="dewayne-boto3-06212024", Key="test_text2.txt", Body="Hey this is a string", ContentType="text/plain")
print("File uploaded successfully.")