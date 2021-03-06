#!/usr/bin/python3

import cgi
import subprocess as spb
import os

print('content-type:text/html')
print()

def putFiles(FILE , ip_) : 
  
   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m command -a"rm /etc/hadoop/{FILE}.xml"')

   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m copy -a"src=/ctemp/{FILE}.xml dest=/etc/hadoop"')

   #sc = spb.getstatusoutput(f'rm /var/www/cgi-bin/{FILE}.xml')


def buildNode(dis) :
    
    mode , IP , IP_master , file_name , port_number , wanttocreateLV , wanttocreateVG , vg_name , n_harddisk , harddisk_names , lv_name , lv_size , furtherSpace ,add_space, runService = dis

    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'

    ANS = 'sudo /usr/local/bin/ansible all -m'
    print('Processing.......')
    print('hello')
   
    installations = [
                      f'{ANS} copy -a"src=/root/{jdk} dest=/root"',
                      f'{ANS} copy -a"src=/root/{hadoop} dest=/root"',
                      f'{ANS} command -a"rpm -i {jdk}"',
                      f'{ANS} command -a"rpm -i {hadoop} --force"', 
                    ]
    
    #for op in installations : status = spb.getstatusoutput(op)
    status = [0]
    print('Hadoop installed successfully!' if status[0]==0 else 'Failed to install Hadoop!')

    #Building the file
    if mode == 'datanode' : 
        print(1)
        filestatus = spb.getstatusoutput(f'{ANS} command -a"mkdir /{file_name}"')
        print(2)
        if wanttocreateLV == 'Yes': 
              
           
            print(3)
            if wanttocreateVG == 'Yes':
               
               
               print(4)
               vg = f'vgcreate {vg_name}'
            
               print(4)
               for i_ in range(n_harddisk) :
                    print(5)
                   #print(f'{ANS} command -a"pvcreate {harddisk_names[i_]}"')
                    status = spb.getstatusoutput(f'{ANS} command -a"pvcreate {harddisk_names[i_]}"')
                    vg += ' ' + harddisk_names[i_]
               
               status = spb.getstatusoutput(f'{ANS} command -a"{vg}"')

            
            
            lv_path = f'/dev/{vg_name}/{lv_name}'
           
            status = spb.getstatusoutput(f'{ANS} command -a"lvcreate --size {lv_size}G --name {lv_name} {vg_name}"')
            
            print(f'logical volume {lv_name} created!' if status[0]==0 else 'Failed to create logical volume!')
             
            status = spb.getstatusoutput(f'{ANS} command -a"mkfs.ext4 {lv_path}"')
            status = spb.getstatusoutput(f'{ANS} command -a"mount {lv_path} /{file_name}"')

            print('Partition -> Format -> Mount Done!' if status[0]==0 else 'Error!')

            
            
            if furtherSpace ==  'Yes' : 
             
                if reduceOther == 'Yes':

                    rCommands = [
                                  f'unmount {dpath}',
                                  f'e2fsck -f {dpath}',
                                  f'resize2fs {dpath} {size_till}G',
                                  f'lvreduce --size -{msize}G {dpath}'
                                  f'mount {dpath} {dmp}'   
                                ]

                    for insc in rCommands : 
                          status = spb.getstatusoutput(f'{ANS} command -a"{insc}"')  
                
                status = spb.getstatusoutput(f'{ANS} command -a"lvextend --size +{add_space}G {lv_path}"')
                status = spb.getstatusoutput(f'{ANS} command -a"resize2fs {lv_path}"')
                
                print(f'logical volume {lv_name} extented by {add_space}GiB' if status[0]==0 else 'Failed to extend logical volume!')
            
            

    #Creating core-site file
    ip = IP_master
    vz = spb.getstatusoutput('sudo cp /root/core-site.xml /ctemp')
    vz = spb.getstatusoutput('sudo chown apache /ctemp/core-site.xml')

    core_ins = [
                '\<configuration\> ',

                '',

                '\<property\> ',

                '\<name\>fs.default.name\</name\> ',

                f'\<value\>hdfs://{ip}:{port_number}\</value\> ',

                '\</property\> ',

                '',

                '\</configuration\> '
               ]

      

    for ins in core_ins : 
        cs =  spb.getstatusoutput(f'sudo echo {ins} >> /ctemp/core-site.xml')       
   
    
    
    #creating hdfs-site file
    if mode == 'datanode' : 
       vz = spb.getstatusoutput('sudo cp /root/hdfs-site.xml /ctemp')
       vz = spb.getstatusoutput('sudo chown apache /ctemp/hdfs-site.xml')


       F =  file_name 

       hdfs_ins = [
                   '\<configuration\> ',

                   '',

                   '\<property\> ',

                   f'\<name\>dfs.data.dir\</name\> ',

                   f'\<value\>/{F}\</value\> ',

                   '\</property\> ',

                   '',

                   '\</configuration\> '
                  ]


     
       for ins_ in hdfs_ins : 
          
            cs = spb.getstatusoutput(f'sudo echo {ins_} >> /ctemp/hdfs-site.xml')
       
       
       putFiles('hdfs-site' , IP)


    #deleating and sending new files

    putFiles('core-site' , IP)

    print('core-site.xml and hdfs-site.xml configured successfully!')
    

    
    if runService == 'Yes' :
   
            sc = spb.getstatusoutput(f'{ANS} command -a"hadoop-daemon.sh start {mode}"')
            print(f'{mode} launched!' if sc[0] == 0 else 'Failed to launch!')
            

        
  
################################################################################


form_values = cgi.FieldStorage()

IP = form_values.getvalue('ip_')
IP_master = form_values.getvalue('mip_')
file_name = form_values.getvalue('fn_')
port_number = form_values.getvalue('pn')

wanttocreateLV = form_values.getvalue('lv')
wanttocreateVG = form_values.getvalue('vg')
vg_name = form_values.getvalue('vgn')
n_harddisk = int(form_values.getvalue('nhd'))
harddisk_names = form_values.getvalue('HDD').split(' ')
lv_name = form_values.getvalue('lvn')
lv_size = int(form_values.getvalue('lvs'))
furtherSpace = form_values.getvalue('ads')
add_space = int(form_values.getvalue('ADS'))
runService = form_values.getvalue('ssv')

DIS = ['datanode' , IP , IP_master , file_name , port_number , wanttocreateLV , wanttocreateVG , vg_name , n_harddisk , harddisk_names , lv_name , lv_size , furtherSpace ,add_space , runService]


buildNode(DIS) 