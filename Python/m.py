#!/usr/bin/python3

import cgi
import subprocess as spb

print("content-type:text/plain")
print()

form_values = cgi.FieldStorage()
cmd = form_values.getvalue("v")

cmd = cmd.lower()

if 'free -m' in cmd or 'free ram' in cmd : 
    process_output = spb.getoutput('free -m')

elif 'date' in cmd : 
    process_output = spb.getoutput('date')

elif 'cal' in cmd or 'calendar' in cmd : 
    process_output = spb.getoutput('cal')

elif 'lscpu' in cmd  or 'cpu details' in cmd : 
    process_output = spb.getoutput('sudo lscpu')

elif 'drop cash' in cmd :
    process_output = spb.getoutput('sudo echo 3 > /proc/sys/vm/drop_caches')

elif 'df -h' in cmd or 'memory information' in cmd : 
     process_output = spb.getoutput('sudo df -h')

elif 'systemctl status httpd' in cmd or 'server status' in cmd:
     process_output = spb.getoutput('sudo systemctl status httpd')

elif 'systemctl status docker' in cmd or 'docker status' in cmd :
     process_output = spb.getoutput('sudo systemctl status docker')

elif 'ps -aux' in cmd or 'running processes' in cmd : 
     process_output = spb.getoutput('sudo ps -aux')

elif 'netstat -tnlp' in cmd  or 'ports' in cmd : 
     process_output = spb.getoutput('sudo netstat -tnlp')

elif 'ifconfig enp0s3' in cmd or 'ip configuration' in cmd :
    process_output = spb.getoutput('sudo ifconfig enp0s3')

print(process_output)