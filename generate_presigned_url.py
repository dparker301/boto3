import boto3

# Calling the client
s3 = boto3.client('s3')

# Generating a presigned url for the s3 file test_test.txt. The access will expire in 1mins (60*5 = 300sec)
response = s3.generate_presigned_url('get_object', Params={'Bucket': "dewayne-boto3-06212024", 'Key': "test_text.txt"}, ExpiresIn=300)
                                                    
print(response)

