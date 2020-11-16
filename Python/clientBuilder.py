#!/usr/bin/python3

import cgi
import subprocess as spb

print('content-type:text/html')
print()


def putFiles(fi):

    
   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m command -a"rm /etc/hadoop/{fi}.xml"')

   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m copy -a"src=/ctemp/{fi}.xml dest=/etc/hadoop"')

   #sc = spb.getstatusoutput(f'rm /var/www/cgi-bin/{fi}.xml')

  

def buildClient(A) :
    
    remoteIP,masterIP,port_number,changeSettings,RF,BS = A
     
    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'

    ANS = 'sudo /usr/local/bin/ansible all -m'
    print('Processing.......')
 

    installations = [
                      f'{ANS} copy -a"src=/ctemp/{jdk} dest=/root"',
                      f'{ANS} copy -a"src=/ctemp/{hadoop} dest=/root"',
                      f'{ANS} command -a"rpm -i {jdk}"',
                      f'{ANS} command -a"rpm -i {hadoop} --force"',
                    ]

    for op in installations : status = spb.getstatusoutput(op)

    if changeSettings == 'Yes' :

          cs = spb.getstatusoutput(f'sudo cp /root/hdfs-site.xml /ctemp')
          vz = spb.getstatusoutput('sudo chown apache /ctemp/hdfs-site.xml')


          client_ins=['\<configuration\>' , '' , '\<property\>' ,
                      '\<name\>dfs.replication\</name\>' , f'\<value\>{RF}\</value\>',                      '\</property\>' , '' , '\<property\>' ,
                      '\<name\>dfs.block.size\</name\>' , f'\<value\>{BS}\</value\>',                       '\</property\>' , '' , '\</configuration\>']

          for c_li in client_ins :
                write = spb.getstatusoutput(f'echo {c_li} >> /ctemp/hdfs-site.xml')


          putFiles('hdfs-site')

    cs = spb.getstatusoutput(f'sudo cp /root/core-site.xml /ctemp')
    vz = spb.getstatusoutput('sudo chown apache /ctemp/core-site.xml')


    core_ins = [
                '\<configuration\> ',

                '',

                '\<property\> ',

                '\<name\>fs.default.name\</name\> ',

                f'\<value\>hdfs://{masterIP}:{port_number}\</value\> ',

                '\</property\> ',

                '',

                '\</configuration\> '
               ]
    
    for ins in core_ins :
           cs = spb.getstatusoutput(f'sudo echo {ins} >> /ctemp/core-site.xml')

    
    putFiles('core-site')
    print('Client configured!')


form_values = cgi.FieldStorage()
remoteIP = form_values.getvalue('ip_')
masterIP = form_values.getvalue('mip_')
port_number = int(form_values.getvalue('pn'))
changeSettings = form_values.getvalue('ssv')

RF = int(form_values.getvalue('rf_'))

BS = int(form_values.getvalue('bs'))

#print(port_number,RF)

buildClient([remoteIP,masterIP,port_number,changeSettings,RF,BS])


