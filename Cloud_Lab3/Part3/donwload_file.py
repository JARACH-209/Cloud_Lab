import boto3

s3 = boto3.resource("s3")
bucket_name = "achalbuck2"

s3 = boto3.resource('s3')

# select bucket
my_bucket = s3.Bucket(bucket_name)

# download file into current directory
for s3_object in my_bucket.objects.all():
        # Need to split s3_object.key into path and file name, else it will give error file not found.
            path, filename = os.path.split(s3_object.key)
                my_bucket.download_file(s3_object.key, filename,"/var/www/html")
#detination for all the files is "/var/www/html"
