#!/usr/bin/python3

import cgi
from subprocess import getstatusoutput as gso

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()
mode = form_values.getvalue('i0')
AWS = 'sudo /usr/local/bin/aws'

if mode == 'start instance' : 

   id = form_values.getvalue('i1')
   status = gso(f'{AWS} ec2 start-instances --instance-ids {id}')
   print('ec2 instance started!' if status[0]==0 else 'Failed to start!')

elif mode == 'stop instance' :
  
   id = form_values.getvalue('i1')
   status = gso(f'{AWS} ec2 stop-instances --instance-ids {id}')
   print('ec2 instance stopping!' if status[0]==0 else 'Failed to stop!')

elif mode == 'create SG':
   
   group_name = '"'+form_values.getvalue('i1')+'"'
   group_des =  '"'+form_values.getvalue('i2')+'"'

   status = gso(f'{AWS} ec2 create-security-group --description {group_des} --group-name {group_name}')
   print('security group created!' if status[0]==0 else 'Failed to create SG!')

elif mode == 'create S3' : 

   bucket_name = form_values.getvalue('i1')
   region = form_values.getvalue('i2')

   status = gso(f'{AWS} s3api create-bucket --bucket {bucket_name} --region {region} --create-bucket-configuration LocationConstraint={region}')
   print('Bucket created!' if status[0]==0 else 'Failed to create bucket!')   

elif mode == 'upload to bucket' : 

   bucket_name = form_values.getvalue('i1')
   path = form_values.getvalue('i2')
   status = gso(f'{AWS} s3 cp {path} s3://{bucket_name}/')
   print('file uploaded to bucket!' if status[0]==0 else 'Failed to upload!')

elif mode == 'create cdn' : 
    
   origin = form_values.getvalue('i1')
   status = gso(f'{AWS} cloudfront create-distribution --origin-domain-name {origin}')
   print('Distribution created!' if status[0]==0 else 'Failed to create distribution')

