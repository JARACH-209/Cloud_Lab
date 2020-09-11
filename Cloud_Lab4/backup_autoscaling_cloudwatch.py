import boto3
from datetime import datetime
from msvcrt import getch

autoS_client = boto3.client('autoscaling')  #created an autoscaling client
ec2 = boto3.resources('ec2')
cloudwatch = boto3.client('cloudwatch')

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

print("\nCreating Launch Configuration for Autoscaling...\n")

lauch_config = autoS_client.create_launch_configuration(
        LaunchConfigurationName = "lab4_as_launch_config",
        ImageId='ami-07c8bc5c1ce9598c3',        #ami of the instance
        InstanceType = 't2.micro',
        KeyName = keyname, 
        UserData = script, 
        SecurityGroups=['boto3users'], 
        )  

print("\nCreating Autoscaling group...\n")

autos_group = autoS_client.create_auto_scaling_group(
        AutoScalingGroupName='lab4_as_group',
        LaunchConfigurationName='lab4_as_launch_config',
        AvailabilityZones=['us-east-2a','us-east-2b','us-east-2c'], 
        MaxSize=3,         #set the max count to 3 for scaling up to max 3 instances in a group
        MinSize=1   
        )

print("\nCreating Autoscaling group policies...\n")

scale_out_policy = autoS_client.put_scaling_policy(
        AutoScalingGroupName='lab4_as_group',
        PolicyName='scale_out_policy_lab4',          #default is SimpleScaling in PolicyType
        AdjustmentType='ChangeInCapacity',       #changeincapacity will add the given adjustment, ExactCapacity will adjust to the given value and PercentageChaengeInCapacity will change by percentage given     
        ScalingAdjustment=1,                    #only 1 additional instace will be added
        )

scale_in_policy = autoS_client.put_scaling_policy(
        AutoScalingGroupName='lab4_as_group',
        PolicyName='scale_in_policy_lab4',          #default is SimpleScaling in PolicyType
        AdjustmentType='ChangeInCapacity',       #changeincapacity will add the given adjustment, ExactCapacity will adjust to the given value and PercentageChaengeInCapacity will change by percentage given     
        ScalingAdjustment= -1,                    #only removes 1 instace will be added
        )

policy_desc = autoS_client.describe_policies(
        AutoScalingGroupName='lab4_as_group',
        PolicyNames=['scale_in_policy_lab4','scale_out_policy_lab4']
        )

scale_in_arn = None
scale_out_arn = None

for each in policy_desc['ScalingPolicies']:          #policy_description is a dictionary of lists which have disctionaries
    if each['PolicyName'] == 'scale_in_policy_lab4': #we need policy ARNs to set cloudwatch alarms
        scale_in_arn = each['PolicyARN']
    if each['PolicyName'] == 'scale_out_policy_lab4':
        scale_out_arn = each['PolicyARN']

print("\nSetting up cloudwatch alarms...\n")

scale_in_alarn = cloudwatch.put_metric_alarm(
        AlarmName='scale_in_Alarm',
        ComparisonOperator='LessThanThreshold',     #scale in
        EvaluationPeriods=1,                        #no of evaluations that will occur before triggering the alarm
        MetricName= 'NetworkIn',     # using NetworkIn not using CPUUTILIZATION because we are hosting website          
        Namespace='AWS/EC2',
        Period=60,      #monitoring period in seconds before trigger
        Threshold=40.0, #scale-in when traffic is less than 40
        AlarmDescription='Alarm when the website traffic is less than 40 percent',
        Dimensions=[
            {
                'Name':'AutoScalingGroupName',
                'Value':'lab4_as_group'
            },
            ],
        Statistic='Average',
        AlarmActions=[scale_in_arn]
        ) 

scale_out_alarm = cloudwatch.put_metric_alarm(
        AlarmName='scale_out_Alarm',
        ComparisonOperator='GreaterThanThreshold',     #scale out
        EvaluationPeriods=1,                        #no of evaluations that will occur before triggering the alarm
        MetricName= 'NetworkIn',     # using NetworkIn not using CPUUTILIZATION because we are hosting website          
        Namespace='AWS/EC2',
        Period=60,      #monitoring period in seconds before trigger
        Threshold=85.0, #scale-out when traffic is more than 85 percent
        AlarmDescription='Alarm when the website traffic is more than 85 percent',
        Dimensions=[
            {
                'Name':'AutoScalingGroupName',
                'Value':'lab4_as_group'
            },
            ],
        Statistic='Average',
        AlarmActions=[scale_out_arn]
        ) 

print("\nWaiting for instace to be in running state to attach with Autoscaling Group...\n")
instance.wait_until_running()
instance.load()

attach_inst = autoS_client.attach_instances(
        InstanceIds=[str(instance.id)],
        AutoScalingGroupName='lab4_as_group')

print("Public DNS (IPv4): " + instance.public_dns_name)
with open("Instance_DNS.txt","a") as out:
    dt = datetime.now()
    out.write("Instance created : ",dt)
    print("\nInstance name : ",keyname,"\n",file=out)
    print("Public DNS (IPv4): ",instance.public_dns_name,file=out)
    print("-------------------------------------------------",file=out)



