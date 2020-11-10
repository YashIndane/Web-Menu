#!/usr/bin/python3

import cgi
import subprocess as spb

print('content-type:text/plain')
print()

def putFiles(FILE , ip_) : 
  
   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m command -a"rm /etc/hadoop/{FILE}.xml"')

   sc = spb.getstatusoutput(f'sudo /usr/local/bin/ansible all -m copy -a"src=/var/www/cgi-bin/{FILE}.xml /etc/hadoop"')

   sc = spb.getstatusoutput(f'rm /var/www/cgi-bin/{FILE}.xml')


def buildNode(dis) :
    
    mode , IP , IP_master , file_name , port_number , wanttocreateLV , wanttocreateVG , vg_name , n_harddisk , harddisk_names , lv_name , lv_size , furtherSpace ,add_space, runService = dis

    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'

    ANS = 'sudo /usr/local/bin/ansible all -m'
   
    installations = [
                      f'{ANS} copy -a"src=/root/{jdk} dest=/root"',
                      f'{ANS} copy -a"src=/root/{hadoop} dest=/root"',
                      f'{ANS} command -a"rpm -i {jdk}"',
                      f'{ANS} command -a"rpm -1 {hadoop} --force"', 
                    ]

    for op in installations : status = spb.getstatusoutput(op)
   
    print('Hadoop installed successfully!' if status[0]==0 else 'Failed to install Hadoop!')

    #Building the file
    if mode == 'datanode' : 

        filestatus = spb.getstatusoutput(f'{ANS} command -a"mkdir /{file_name}"')
        
        if wanttocreateLV == 'Yes': 
              
           
            
            if wanttocreateVG == 'Yes':
               
               
               
               vg = f'vgcreate {vg_name}'
            

               for i_ in range(n_harddisk) : 
                    
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
             
         
                
                status = spb.getstatusoutput(f'{ANS} command -a"lvextend --size +{add_space}G {lv_path}"')
                status = spb.getstatusoutput(f'{ANS} command -a"resize2fs {lv_path}"')
                
                print(f'logical volume {lv_name} extented by {add_space}GiB' if status[0]==0 else 'Failed to extend logical volume!')
            
            

    #Creating core-site file
    ip = IP_master

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

    cs = spb.getstatusoutput('cp /root/core-site.xml /var/www/cgi-bin')

    for ins in core_ins : 
           cs = spb.getstatusoutput('echo ' + ins + '>> core-site.xml')

    
    #creating hdfs-site file
    if mode == 'datanode' : 

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

       cs = spb.getstatusoutput('cp /root/hdfs-site.xml /var/www/cgi-bin')
     
       for ins_ in hdfs_ins : 
          
            cs = spb.getstatusoutput('echo ' + ins_ + '>> hdfs-site.xml')
       
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
