#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()


form_values = cgi.FieldStorage()

no_of_datanodes = int(form_values.getvalue("nodn"))
no_of_tasktracker = int(form_values.getvalue("nott"))

status = gso("sudo chown apache /details.yml")

#datanodes
status = gso('sudo echo "datanodes:" >> /details.yml')
for i in range(no_of_datanodes):
  status = gso(f'sudo echo " - dn{i}" >> /details.yml')

#tasktrackers
status = gso('sudo echo "tasktrackers:" >> /details.yml')
for j in range(no_of_tasktracker):
  status = gso(f'sudo echo " - tt{j}" >> /details.yml')

#running the playbooks
#launch ec2-instances
status = gso("sudo /usr/local/bin/ansible-playbook /ansible-scripts/ec2-driver.yml")

#configure the nodes
status = gso("sudo /usr/local/bin/ansible-playbook /ansible-scripts/dcc.yml")

print(status)
