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

elif 'systemctl status' in cmd or 'status of' in cmd :
    x = cmd.split(' ')[-1]
    process_output = spb.getoutput('sudo systemctl status ' + x)

elif 'systemctl start' in cmd or 'start' in cmd : 
    y = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl start ' + y)
    print(y + ' started sucessfully!' if process_output[0] == 0 else 'Failed!')

elif 'systemctl stop' in cmd or 'stop' in cmd : 
    z = cmd.split(' ')[-1]
    process_output = spb.getstatusoutput('sudo systemctl stop ' + z)
    print(y + ' stopped sucessfully!' if process_output[0] == 0 else 'Failed!')

elif 'drop cash' in cmd :
    process_output = spb.getoutput('sudo echo 3 > /proc/sys/vm/drop_caches')

elif 'df -h' in cmd or 'memory information' in cmd : 
     process_output = spb.getoutput('sudo df -h')

elif 'ps -aux' in cmd or 'running processes' in cmd : 
     process_output = spb.getoutput('sudo ps -aux')

elif 'netstat -tnlp' in cmd  or 'ports' in cmd : 
     process_output = spb.getoutput('sudo netstat -tnlp')

elif 'ifconfig enp0s3' in cmd or 'ip configuration' in cmd :
    process_output = spb.getoutput('sudo ifconfig enp0s3')

elif 'fdisk -l' in cmd or 'show hard disk' in cmd:
    process_output = spb.getoutput('sudo fdisk -l')

elif 'route -n' in cmd or 'show route table' in cmd:
    process_output = spb.getoutput('sudo route -n')

elif 'pvdisplay' in cmd or 'show physical volume' in cmd:
    process_output = spb.getoutput('sudo pvdisplay')

elif 'vgdisplay' in cmd or 'show volume group' in cmd : 
    process_output = spb.getoutput('sudo vgdisplay')

elif 'lvdisplay' in cmd or 'show logical volume' in cmd:
    process_output = spb.getoutput('sudo lvdisplay')

elif 'lsblk' in cmd or 'show partitions' in cmd:
    process_output = spb.getoutput('sudo lsblk')

elif 'history' in cmd or 'show history' in cmd :
    process_output = spb.getoutput('history')



print(process_output)

