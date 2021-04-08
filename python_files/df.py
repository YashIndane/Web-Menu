#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

content = form_values.getvalue("co")
name_of_image = form_values.getvalue("na")
image_version = form_values.getvalue("ver")
username = form_values.getvalue("user")
password = form_values.getvalue("pass")

path = f'/dockerfiles/{name_of_image}'

status = gso(f'sudo mkdir {path}')
status = gso(f'sudo touch {path}/Dockerfile')
status = gso(f'sudo chown apache {path}/Dockerfile')
status = gso(f'sudo echo "{content}" >> {path}/Dockerfile')
status = gso(f'sudo dos2unix {path}/Dockerfile')
status = gso('sudo systemctl start docker')
status = gso(f'sudo docker build -t {username}/{name_of_image}:{image_version} {path}')
status = gso(f'sudo docker login -u {username} -p {password}') 
status = gso(f'sudo docker push {username}/{name_of_image}:{image_version}')

print(status)

