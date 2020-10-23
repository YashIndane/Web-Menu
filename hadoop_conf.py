#!/usr/bin/python3
import subprocess as spb

IP = input("Enter the IP of remote system -> ")
conf = input("Configuration type -> ")

if conf.lower() == 'datanode' : 

    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'
   
    operations = [
                  f'scp /root/{jdk} {IP}:/root' ,
                  f'scp /root/{hadoop} {IP}:/root',
                  f'ssh {IP} rpm -i {jdk}' ,
                  f'ssh {IP} rpm -i {hadoop} --force' 
                 ]

    for op in operations : 
          
           status = spb.getstatusoutput(op)
           

   
