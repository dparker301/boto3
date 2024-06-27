import boto3

# Imported the boto3 library and set up an S3 client. This client will allow me to interact with Amazon S3
s3 = boto3.client('s3')


s3.upload_file('/home/ec2-user/environment/boto3/boto3/test_text.txt', 'dewayne-boto3-06212024', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})
print("File uploaded successfully.")