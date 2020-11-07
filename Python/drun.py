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

elif 'stop docker' in cmd:
 
   s = gso('sudo systemctl stop docker')
   print('Docker stopped sucessfully' if s[0]==0 else 'Failed to stop docker!')

elif 'launch os' in cmd :
  
  s = gso(f'sudo docker run -d -i -t --name {osname} {osimage}')
  print('OS launched sucessfully!' if s[0] == 0 else 'Failed to launch!')

elif 'docker state' in cmd :
   
   print(gso('sudo docker ps')[1])

elif 'docker pull' in cmd : 
   
   os = cmd.split(' ')[-1]
   s = gso('sudo ' + 'docker pull ' + os)
   print(os + 'downloaded sucessfully!' if s[0] == 0 else 'Failed to download!')

elif 'available images' in cmd: 
 
   print(f'''--------------DOCKER-IMAGES---------------\n
         {gso('sudo docker images')[1]}''')

elif 'docker status' in cmd : 
 
   print(f'''--------------DOCKER-STATUS---------------\n
         {gso('sudo systemctl status docker')[1]}''')

else : 

  s = gso('sudo ' + cmd)
  print(s[1] if s[0]==0 else 'Failed')
