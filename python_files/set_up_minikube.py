#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

remote_ip = form_values.getvalue('-ip-')
passwd = form_values.getvalue('pw')

status = gso('sudo touch /inven.txt')
status = gso('sudo chown apache /inven.txt')

status = gso('sudo /usr/bin/echo "[minikube_ip]" >> /inven.txt')
status = gso(f'sudo /usr/bin/echo "{remote_ip} ansible_user=root ansible_ssh_pass={passwd} ansible_connection=ssh" >> /inven.txt')
status = gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/mini.yml')

print('successful' if status[0]==0 else 'failed')
