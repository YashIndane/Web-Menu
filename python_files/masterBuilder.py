#!/usr/bin/python3

import cgi
import subprocess as spb

print('content-type:text/html')
print()

def putFiles(FILE) :

   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m shell -a"rm /etc/hadoop/{FILE}.xml"')

   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m copy -a"src=/ctemp/{FILE}.xml dest=/etc/hadoop"')

   #sc = spb.getstatusoutput(f'rm /var/www/cgi-bin/{FILE}.xml')

def buildMaster(Z):

    remoteIP,filename,port_number,startService = Z

   
    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'

    ANS = 'sudo /usr/local/bin/ansible all -m'
    print('Processing.......')
   

    installations = [
                      f'{ANS} copy -a"src=/ctemp/{jdk} dest=/root"',
                      f'{ANS} copy -a"src=/ctemp/{hadoop} dest=/root"',
                      f'{ANS} shell -a"rpm -i /root/{jdk}"',
                      f'{ANS} shell -a"rpm -i /root/{hadoop} --force"',
                    ]

    for op in installations : status = spb.getstatusoutput(op)

    print("hadoop and jdk installed successfully!")
    
    vz = spb.getstatusoutput('sudo cp /root/core-site.xml /ctemp')
    vz = spb.getstatusoutput('sudo chown apache /ctemp/core-site.xml')


    core_ins = [
                '\<configuration\> ',

                '',

                '\<property\> ',

                '\<name\>fs.default.name\</name\> ',

                f'\<value\>hdfs://{remoteIP}:{port_number}\</value\> ',

                '\</property\> ',

                '',

                '\</configuration\> '
               ]

    for ins in core_ins :
        cs =  spb.getstatusoutput(f'sudo echo {ins} >> /ctemp/core-site.xml') 

    putFiles('core-site')

    vz = spb.getstatusoutput('sudo cp /root/hdfs-site.xml /ctemp')
    vz = spb.getstatusoutput('sudo chown apache /ctemp/hdfs-site.xml')
   

    hdfs_ins = [
                   '\<configuration\> ',

                   '',

                   '\<property\> ',

                   f'\<name\>dfs.name.dir\</name\> ',

                   f'\<value\>/{filename}\</value\> ',

                   '\</property\> ',

                   '',

                   '\</configuration\> '
                  ]
   
    for ins_ in hdfs_ins :

            cs = spb.getstatusoutput(f'sudo echo {ins_} >> /ctemp/hdfs-site.xml')

    putFiles('hdfs-site')

    filestatus = spb.getstatusoutput(f"{ANS} shell -a'mkdir /{filename}'")
           
    filestatus = spb.getstatusoutput(f"{ANS} shell -a'echo Y | hadoop namenode -format'")

   

    if startService == 'Yes': 
             
       sc = spb.getstatusoutput(f"{ANS} shell -a'hadoop-daemon.sh start namenode'")
       fire_wall = spb.getstatusoutput(f"{ANS} firewalld -a'port={port_number}/tcp state=enabled immediate=yes'")
       print(f'namenode launched!' if sc[0] == 0 else 'Failed to launch!')
    
   
 
################################################################################

form_values = cgi.FieldStorage()
remoteIP = form_values.getvalue('ri')
filename = form_values.getvalue('fn')
port_number = form_values.getvalue('pn')
startService = form_values.getvalue('stv')

buildMaster([remoteIP,filename,port_number,startService])