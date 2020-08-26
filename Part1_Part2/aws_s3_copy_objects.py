import boto3

s3 = boto3.resource("s3")

def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
            'Bucket': bucket_from_name,
            'Key': file_name
            }
    s3.Object(bucket_to_name, file_name).copy(copy_source)

first_bucket_name = input("\nEnter the source bucket name\n")
second_bucket_name = input("\nEnter the destination bucket name\n")
file_name = input("\nEnter the name of the file to be copied\n")

copy_to_bucket(first_bucket_name, second_bucket_name, file_name)

print("\nFile Copied Successfully\n")
