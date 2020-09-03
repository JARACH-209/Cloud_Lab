import boto3
from datetime import datetime

ec2  = boto3.resource("ec2")


with open("startup.sh", 'r') as f:
    script = f.read()

keyname = "Cloud_Lab0"      #key pair name from cosole

print("\nCreating Instance...\n")

instances = ec2.create_instances(
        ImageId='ami-07c8bc5c1ce9598c3',        #ami of the instance
        InstanceType = 't2.micro',
        KeyName = keyname, 
        UserData = script, 
        SecurityGroups=['boto3users'], 
        MinCount=1, 
        MaxCount=1  )

instance = instances[0]
print("\nInstance created waiting for running state\n")

instance.wait_until_running()
instance.load()
print("Public DNS (IPv4): " + instance.public_dns_name)
with open("Instance_DNS.txt","a") as out:
    dt = datetime.now()
    out.write("Instance created : "+str(dt)+"\n")
    print("Instance name : ",keyname,"\n",file=out)
    print("Public DNS (IPv4): ",instance.public_dns_name)
    print("-------------------------------------------------")




