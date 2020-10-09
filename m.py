#!/usr/bin/python3

import cgi
import subprocess as spb

print("content-type:text/plain")
print()

form_values = cgi.FieldStorage()
cmd = form_values.getvalue("v")

cmd = cmd.lower()

if 'free ram' in cmd : 
    process_output = spb.getoutput('free -m')

elif 'date' in cmd : 
    process_output = spb.getoutput('date')

elif 'calendar' in cmd : 
    process_output = spb.getoutput('cal')

elif 'ip configuration' : 
    process_output = spb.getoutput('sudo ifconfig enp0s3')

elif 'cpu details' in cmd : 
    process_output = spb.getoutput('sudo lscpu')

elif 'drop cash' in cmd :
    process_output = spb.getoutput('sudo echo 3 > /proc/sys/vm/drop_caches')

print(process_output)









