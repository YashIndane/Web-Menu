#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

cmd = form_values.getvalue('dcmd').lower()
osname = form_values.getvalue('osname')
osimage = form_values.getvalue('img')


if 'start docker' in cmd: 

  s = gso('sudo systemctl start docker')
  print('Docker started sucessfully!' if s[0]==0 else 'Failed to start docker!')

 
