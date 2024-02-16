import boto3

s3 = boto3.client("s3", region_name="us-west-2")

s3.delete_object(Bucket="coulterlearning", Key="example1.txt")