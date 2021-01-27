#!/usr/bin/python3

import cgi
from subprocess import getstatusoutput as spb

print('content-type:text/html')
print()

def createServer(X):

 remoteIP , targetIP , file , permi , ss , mountFile = X

 status = spb('sudo mkdir /ctemp/exports')
 status = spb('sudo chown apache /ctemp/exports')

 ANS = 'sudo /usr/local/bin/ansible' 

 status = spb(f'{ANS} {remoteIP} -m  shell -a"mkdir /{file}"')
 
 if permi == 'Read-Write' : 
    A = f'"/{file} {targetIP} (rw,no_root_squash)"'

 else :
    A = f'"/{file} {targetIP} (ro)"'
 
 status = spb(f'sudo echo {A} >> /ctemp/exports')
 status = spb(f'{ANS} {remoteIP} -m copy -a"src=/ctemp/exports dest=/etc"')  

 print('NFS-server successfully configured!' if status[0]==0 else 'Failed to configure!')

 if ss == 'Yes' : 
    status = spb(f'{ANS} {remoteIP} -m shell -a"systemctl start nfs-server"')
    print('NFS-server started!' if status[0]==0 else 'Failed to start!')
   
    status = spb(f'{ANS} {remoteIP} -m service -a"name=firewalld state=stopped"')
    if status[0] == 0 :
         status = spb(f'{ANS} {targetIP} -m file -a"path=/{mountFile} state=directory"')
         status = spb(f'{ANS} {targetIP} -m service -a"name=firewalld state=stopped"')
         status = spb(f'{ANS} {targetIP} -m mount -a"src={remoteIP}:/{file} path=/{mountFile} fstype=nfs state=mounted"')
         
form_values = cgi.FieldStorage()

remoteIP = form_values.getvalue('rip')
targetIP = form_values.getvalue('gip')
file = form_values.getvalue('ffn')
permi = form_values.getvalue('per')
ss = form_values.getvalue('st')
mountFile = form_values.getvalue('mf')

createServer([remoteIP , targetIP , file , permi , ss , mountFile])