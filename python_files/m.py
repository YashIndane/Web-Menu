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
    
elif 'uptime' in cmd :
    process_output = spb.getstatusoutput('sudo uptime')

elif 'status of' in cmd :
    x = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl status ' + x)

elif 'start' in cmd : 
    y = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl start ' + y)
    print(y + ' started sucessfully!' if process_output[0] == 0 else 'Failed!')

elif 'stop' in cmd : 
    z = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl stop ' + z)
    print(z + ' stopped sucessfully!' if process_output[0] == 0 else 'Failed!')

elif 'drop cash' in cmd :
    process_output = spb.getstatusoutput('sudo echo 3 > /proc/sys/vm/drop_caches')

elif 'memory information' in cmd : 
     process_output = spb.getstatusoutput('sudo df -h')

elif 'running processes' in cmd : 
     process_output = spb.getstatusoutput('sudo ps -aux')

elif 'ports' in cmd : 
     process_output = spb.getstatusoutput('sudo netstat -tnlp')

elif 'ip configuration' in cmd :
    process_output = spb.getstatusoutput('sudo ifconfig enp0s3')

elif 'show hard disk' in cmd:
    process_output = spb.getstatusoutput('sudo fdisk -l')

elif 'show route table' in cmd:
    process_output = spb.getstatusoutput('sudo route -n')

elif 'show physical volume' in cmd:
    process_output = spb.getstatusoutput('sudo pvdisplay')

elif 'show volume group' in cmd : 
    process_output = spb.getstatusoutput('sudo vgdisplay')

elif 'show logical volume' in cmd:
    process_output = spb.getstatusoutput('sudo lvdisplay')

elif 'show partitions' in cmd:
    process_output = spb.getstatusoutput('sudo lsblk')

elif 'show history' in cmd :
    process_output = spb.getstatusoutput('history')

elif 'routing table' in cmd:
    process_output = spb.getstatusoutput('sudo route -n')

else : 
   process_output = spb.getstatusoutput('sudo ' + cmd)
   print("Successful" if process_output[0]==0 else "Failed")
   T = True

print(process_output[1] if T else process_output)
