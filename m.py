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
    process_output = spb.getoutput('free -m')

elif 'date' in cmd : 
    process_output = spb.getoutput('date')
