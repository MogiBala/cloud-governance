import json
with open ("ec2.js", "r") as ec2_file:  #parsing json
    data = json.load(ec2_file)
inst = data["InstanceType"]             #assigning ec2 instance type to other variable
print(inst)

#launching an instance
import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
  ImageId='ami-02bcbb802e03574ba',       #type of instance or AMI ID
  MinCount=1,
  MaxCount=2,
  InstanceType='t2.micro',               # or use inst from above.
  KeyName='ec2-keypair'                  # type of key id_rsa alternative
  )


