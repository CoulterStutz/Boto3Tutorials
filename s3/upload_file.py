import boto3

s3 = boto3.client('s3', region_name='us-west-2')

response = s3.upload_file("example.txt", "coulterlearning", "example.txt")