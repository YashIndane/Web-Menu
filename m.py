#!/usr/bin/python3

import cgi
import subprocess as spb

print("content-type:text/plain")
print()

form_values = cgi.FieldStorage()
cmd = form_values.getvalue("v")

cmd = cmd.lower()
T = False

if 'free ram' in cmd : 
    process_output = spb.getstatusoutput('free -m')

elif 'date' in cmd : 
    process_output = spb.getstatusoutput('date')

elif 'calendar' in cmd : 
    process_output = spb.getstatusoutput('cal')

elif 'cpu details' in cmd : 
    process_output = spb.getstatusoutput('sudo lscpu')

elif 'status of' in cmd :
    x = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl status ' + x)

elif 'start' in cmd : 
    y = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl start ' + y)
    print(y + ' started sucessfully!' if process_output[0] == 0 else 'Failed!')
