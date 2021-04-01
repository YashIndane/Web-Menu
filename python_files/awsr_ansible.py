#!/usr/bin/python3

import cgi
import subprocess

print('content-type:text/html')
print()

form_values = cgi.FieldStorage()

names = [
          ['ins_reg' , 'r1'],
          ['instance_state' , 'i0'],
          ['instance_i' , 'i1']
        ]

x = subprocess.getstatusoutput('sudo chown apache /ansible-scripts/details.yml')

for tag , n in names:

  l = f'"{tag}: {form_values.getvalue(n)}"'
  x = subprocess.getstatusoutput(f'sudo echo {l} >> /ansible-scripts/details.yml ')

x = subprocess.getstatusoutput('sudo /usr/local/bin/ansible-playbook /ansible-scripts/start_ins.yml')

print(x)
