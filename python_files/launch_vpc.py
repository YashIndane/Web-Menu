#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

names = [
          [ 'vpc_name'  , 'vpcn' ],
          [ 'vpc_cidr' , 'vpcc' ],
          [ 'subnet_name1' , 'su1' ],
          [ 'subnet_name2', 'su2' ]
          [ 'subnet_cidr1', 'sc1' ]
          [ 'subnet_cidr2', 'sc2' ]
          [ 'instance_name1', 'ec1' ]
          [ 'instance_name2', 'ec2' ]
        ]

x = gso('sudo chown apache /ansible-scripts/details.yml')

for tag , n in names:
    line = f'"{tag}: {form_values.getvalue(n)}"'
    x = gso(f'sudo echo {line} >> /ansible-scripts/details.yml')

x=gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/launch_vpc.yml')
print(x)