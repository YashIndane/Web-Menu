#!/usr/bin/python3

import cgi
import subprocess

print('content-type:text/html')
print()

form_values = cgi.FieldStorage()

names = [  
          ['group_name' , 'i1'],
          ['des' , 'i2'],
          ['reg' , 'i3']
        ]

x = subprocess.getstatusoutput('sudo chown apache /ansible-scripts/details.yml')

for tag , n in names: 

  l = f'"{tag}: {form_values.getvalue(n)}"'
  x = subprocess.getstatusoutput(f'sudo echo {l} >> /ansible-scripts/details.yml ')

x = subprocess.getstatusoutput('sudo /usr/local/bin/ansible-playbook /ansible-scripts/create_sg.yml')

print(x)

