#!/usr/bin/python3

from subprocess import getstatusoutput as gso
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

cmd = form_values.getvalue('dcmd').lower()
osname = form_values.getvalue('osname')
osimage = form_values.getvalue('img')


if 'systemctl start docker' in cmd or 'start docker' in cmd: 

  s = gso('sudo systemctl start docker')
  print('Docker started sucessfully!' if s[0]==0 else 'Failed to start docker!')

elif 'systemctl stop docker' in cmd or 'stop docker' in cmd:
 
   s = gso('sudo systemctl stop docker')
   print('Docker stopped sucessfully' if s[0]==0 else 'Failed to stop docker!')

elif 'docker run' in cmd :
  
  s = gso(f'sudo docker run -d -i -t --name {osname} {osimage}')
  print('OS launched sucessfully!' if s[0] == 0 else 'Failed to launch!')

elif 'docker stop' in cmd:

   s = gso('sudo ' + cmd)
   print('OS stopped sucessfully!' if s[0] == 0 else 'Failed to stop!')

elif 'docker ps' in cmd or 'docker status' in cmd :
   
   print(gso('sudo docker ps')[1])

elif 'docker images' in cmd or 'available images' in cmd: 
 
   print(f'''--------------DOCKER-IMAGES---------------\n
         {gso('sudo docker images')[1]}''')

elif 'systemctl status docker' in cmd : 
 
   print(f'''--------------DOCKER-STATUS---------------\n
         {gso('sudo ' + cmd)[1]}''')

else : print('NO SUCH COMMAND!')
