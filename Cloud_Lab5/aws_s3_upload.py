<<<<<<< HEAD:Cloud_Lab5/aws_s3_upload.py
import boto3
import logging
import time
from botocore.exceptions import ClientError

'''
def upload_file(file_name, bucket, object_name= None):
    """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('S3')
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True
'''

s3 = boto3.resource('s3')
bucket_name = str(input("\nEnter the bucket name in which uplaod has to be made\n"))

num_file = int(input("\nEnter the number of files\n"))

for each in range(num_file):

	file_name = input("\nEnter the name of file number {} to be uploaded\n".format(each+1))

	#we will upload using an instane of object. We can use high level classes like Bucket or Object
	#or we can simply use client.upload_file

	'''
	s3.meta.client.upload_file( Filename=first_file_name, Bucket=first_bucket_name, Key=first_file_name)
	'''

	#bucket_object = s3.Object(bucket_name = bucket_name, key = file_name)

	flag = s3.meta.client.upload_file(
	            Filename=file_name, Bucket=bucket_name,
	                Key=file_name)
	print("\nFile uploaded Successfully\n")
x = input("Press any key to exit\n")

=======
import boto3
import logging
import time
from botocore.exceptions import ClientError

'''
def upload_file(file_name, bucket, object_name= None):
    """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('S3')
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True
'''

s3 = boto3.resource('s3')
bucket_name = str(input("\nEnter the bucket name in which uplaod has to be made\n"))

num_file = int(input("\nEnter the number of files\n"))

for each in range(num_file):

	file_name = input("\nEnter the name of file number {} to be uploaded\n".format(each+1))

	#we will upload using an instane of object. We can use high level classes like Bucket or Object
	#or we can simply use client.upload_file

	'''
	s3.meta.client.upload_file( Filename=first_file_name, Bucket=first_bucket_name, Key=first_file_name)
	'''

	#bucket_object = s3.Object(bucket_name = bucket_name, key = file_name)

	flag = s3.meta.client.upload_file(
	            Filename=file_name, Bucket=bucket_name,
	                Key=file_name)
	print("\nFile uploaded Successfully\n")
x = input("Press any key to exit\n")

>>>>>>> abd3999597140865603f5fe85fc4434661e0bff0:Cloud_Lab3/Part3/aws_s3_upload.py
