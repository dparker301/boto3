import boto3

# Imported the boto3 library and set up an S3 client. This client will allow me to interact with Amazon S3
s3 = boto3.client('s3')

# Opening the file "test_text.txt" in binary read mode
with open("/home/ec2-user/environment/boto3/test_text.txt", 'rb') as f:

# Use s3.put_object to upload it to the specified bucket.
    s3.put_object(Bucket="dewayne-boto3-06212024", Key="test_text.txt", Body=f, ContentType="text/plain")
    print("File uploaded successfully.")