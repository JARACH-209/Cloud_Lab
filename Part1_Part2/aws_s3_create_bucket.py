#Script to create a AWS S3 Bucket

import boto3
import uuid

s3 = boto3.resource('s3')

def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
                    'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

name = str(input("\nEnter a DNS complaint name-prefix for the Bucket\n"))

bucket_name, response = create_bucket(name, s3.meta.client)

print("\nBucket created successfully\n")
print("\nName : ",bucket_name,"\n")
print("Resource : \n",resource)
print("\n")

