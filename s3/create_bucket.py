import boto3

s3 = boto3.client("s3", region_name="us-west-2")

response = s3.create_bucket(
    ACL='private',
    Bucket='coulterlearning',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
    ObjectLockEnabledForBucket=False,
    ObjectOwnership='BucketOwnerEnforced'
)

print(response)