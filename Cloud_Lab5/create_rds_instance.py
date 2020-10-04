import boto3
rds = boto3.client('rds')

rds_instance = rds.create_db_instance(
				DBInstanceIdentifier = 'lab5',
				MasterUsername = 'boto3_user',
				MasterUserPassword = 'boto3_password',
				DBInstanceClass = 'db.t2.micro',
				Engine = 'mysql',
				AllocatedStorage = 20 		#Allocation in GB Min=20
				)

print("Creating MySQL RDS-DB instance ...")


try:
    dbs = rds.describe_db_instances()
    for db in dbs['DBInstances']:

    	print(db['MasterUsername'], end="    ")
    	print(db['Endpoint']['Address'], end="    ")
    	print(db['Endpoint']['Port'], end="    ")
    	print(db['DBInstanceStatus'], end="    ")
    	with open("RDS_Instance_record.txt",'w') as f:
	    	print(db['MasterUsername'],file=f)
	    	print(db['DBInstanceIdentifier'],file=f)
	    	print(db['Endpoint']['Address'], file=f)
	    	print(db['Endpoint']['Port'], file=f)

except Exception as e:
    print(e)

print("MySQL RDS-DB instance created successfully ")