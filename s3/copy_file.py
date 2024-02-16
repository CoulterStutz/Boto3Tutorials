import boto3

s3 = boto3.client("s3", region_name='us-west-2')

response = s3.copy_object(
    # Destination Definitions
    Bucket='coulterlearning',
    Key='example1.txt',

    # Source Definitions
    CopySource={"Bucket": "coulterlearning", "Key": "example.txt"}
)

print(response)
