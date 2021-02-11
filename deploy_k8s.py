#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

status = gso('sudo chown apache /ansible-scripts/details.yml')

names = [  
          ['kube_master_name' , 'mn'],
          ['kube_worker_name1' , 'w1n'],
          ['kube_worker_name2' , 'w2n']
          ['cidr_block' , 'cdb']
        ]

for tag , n in names: 

  l = f'"{tag}: {form_values.getvalue(n)}"'
  status = gso(f'sudo echo {l} >> /ansible-scripts/details.yml')

cmd = "sudo /usr/local/bin/ansible-playbook"

status = gso(f'{cmd} /ansible-scripts/launching_instances.yml')
status = gso(f'{cmd} /ansible-scripts/master_config.yml')
status = gso(f'{cmd} /ansible-scripts/worker_config.yml')

print(status[0])
