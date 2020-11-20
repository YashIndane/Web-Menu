#!/usr/bin/python3

import cgi
from subprocess import getstatusoutput as spb

print('content-type:text/html')
print()

def createServer(X):

 remoteIP , targetIP , file , permi , ss = X

 status = spb('sudo cp /etc/exports /ctemp')
 status = spb('sudo chown apache /ctemp/exports')

 ANS = 'sudo /usr/local/bin/ansible all -m' 

 status = spb(f'{ANS} command -a"mkdir /{file}"')
 A = f'"/{file} {targetIP} '
 
 A += '(rw,no_root_squash)"' if permi == 'Read-Write' else '(ro)"'

 status = spb(f'sudo echo {A} >> /ctemp/exports')
 status = spb(f'{ANS} copy -a"src=/ctemp/exports dest=/etc"')  

 print('NFS-server successfully configured!' if status[0]==0 else 'Failed to configure!')

 if ss == 'Yes' : 
    status = spb(f'{ANS} command -a"systemctl start nfs-server"')
    print('NFS-server started!' if status[0]==0 else 'Failed to start!')
 
 

form_values = cgi.FieldStorage()

remoteIP = form_values.getvalue('rip')
targetIP = form_values.getvalue('gip')
file = form_values.getvalue('ffn')
permi = form_values.getvalue('per')
ss = form_values.getvalue('st')

createServer([remoteIP , targetIP , file , permi , ss])
