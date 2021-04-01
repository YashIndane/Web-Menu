#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

names = [
          [ 'kube_master_name'  , 'mn' ],
          [ 'kube_worker_name1' , 'w1n' ],
          [ 'kube_worker_name2' , 'w2n' ],
          [ 'cidr_block', 'cdb' ]
        ]

x = gso('sudo chown apache /ansible-scripts/details.yml')

for tag , n in names:
    line = f'"{tag}: {form_values.getvalue(n)}"'
    x = gso(f'sudo echo {line} >> /ansible-scripts/details.yml')

x=gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/launching_instances.yml')
x=gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/master_config.yml')
x=gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/worker_config.yml')

print(x)

