#!/usr/bin/python3

import cgi
import subprocess

print('content-type:text/html')
print()

form_values = cgi.FieldStorage()

names = [  
          ['Load_Balancer' , 'lbn'],
          ['Backend_Server1' , 'bes1'],
          ['Backend_Server2' , 'bes2']
        ]

for tag , n in names: 

  l = f'"{tag}: {form_values.getvalue(n)}"'
  x = subprocess.getstatusoutput(f'sudo echo {l} >> /ansible-scripts/details.yml ')

x = subprocess.getstatusoutput('sudo /usr/local/bin/ansible-playbook /ansible-scripts/main.yml')

print(x)
