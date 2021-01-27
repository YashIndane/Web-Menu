#!/usr/bin/python3
import subprocess as spb




def putFiles(FILE , ip_) : 
  
   sc = spb.getstatusoutput(f'ssh {ip_} rm /etc/hadoop/{FILE}.xml')
   sc = spb.getstatusoutput(f'scp {FILE}.xml {ip_}:/etc/hadoop')
   sc = spb.getstatusoutput(f'rm {FILE}.xml')


def buildNode(mode , IP , PORT , IP2 = 'none', file_='none' , filem_ = 'none') : 

    hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    jdk = 'jdk-8u171-linux-x64.rpm'
   
    installations = [
                     f'scp /root/{jdk} {IP}:/root' ,
                     f'scp /root/{hadoop} {IP}:/root',
                     f'ssh {IP} rpm -i {jdk}' ,
                     f'ssh {IP} rpm -i {hadoop} --force'
                    ]

    for op in installations : status = spb.getstatusoutput(op)
   
    print('Hadoop installed successfully!' if status[0]==0 else 'Failed to install Hadoop!')
    
    #Building the file
    if mode == 'datanode' : 

        filestatus = spb.getstatusoutput(f'ssh {IP} mkdir /{file_}')

        lv_status = input('Do you want to configure storage as logical volume?[Y/N] ')
        if lv_status == 'Y': 
              
            vg_status = input('Want to create volume group?[Y/N] ')
            
            if vg_status == 'Y':
               
               vg_name = input('Enter your VG name -> ')
               
               vg = f'vgcreate {vg_name}'
               no_of_hdd = int(input('Enter number of hard disks -> '))

               for a in range(no_of_hdd) : 
                    hd_n = input('Enter name of hard disk -> ')
                    status = spb.getstatusoutput(f'ssh {IP} pvcreate {hd_n}')
                    vg += ' ' + hd_n
               
               status = spb.getstatusoutput(f'ssh {IP} {vg}')

            else : vg_name = input('Enter your VG name -> ')
            
            lv_name = input('Enter your logical volume name -> ')
            lv_size = int(input('Enter logical volume size in GiB -> '))
            lv_path = f'/dev/{vg_name}/{lv_name}'
           
            status = spb.getstatusoutput(f'ssh {IP} lvcreate --size {lv_size}G --name {lv_name} {vg_name}')
            
            print(f'logical volume {lv_name} created!' if status[0]==0 else 'Failed to create logical volume!')
             
            status = spb.getstatusoutput(f'ssh {IP} mkfs.ext4 {lv_path}')
            status = spb.getstatusoutput(f'ssh {IP} mount {lv_path} /{file_}')
            print('Partition -> Format -> Mount Done!' if status[0]==0 else 'Error!')

            size_up = input('Want to add any further space to LV?[Y/N] ')
            
            if size_up == 'Y' : 
             
                s_u = int(input('Enter space in GiB -> '))
                
                status = spb.getstatusoutput(f'ssh {IP} lvextend --size +{s_u}G {lv_path}')
                status = spb.getstatusoutput(f'ssh {IP} resize2fs {lv_path}')
                
                print(f'logical volume {lv_name} extented by {s_u}GiB' if status[0]==0 else 'Failed to extend logical volume!')
            
            

    #Creating core-site file
    #core-site file configuration is same for client , master , slave
    ip = IP2 if mode in ('datanode' , 'client') else IP

    core_ins = [
                '\<configuration\> ',

                '',

                '\<property\> ',

                '\<name\>fs.default.name\</name\> ',

                f'\<value\>hdfs://{ip}:{PORT}\</value\> ',

                '\</property\> ',

                '',

                '\</configuration\> '
               ]

    cs = spb.getstatusoutput('cp /root/core-site.xml /var/www/cgi-bin')

    for ins in core_ins : 
           cs = spb.getstatusoutput('echo ' + ins + '>> core-site.xml')

    
    #creating hdfs-site file
    if mode in ('datanode' , 'namenode') : 

       X = 'data' if mode == 'datanode' else 'name'
       F =  file_ if mode == 'datanode' else filem_ 

       hdfs_ins = [
                   '\<configuration\> ',

                   '',

                   '\<property\> ',

                   f'\<name\>dfs.{X}.dir\</name\> ',

                   f'\<value\>/{F}\</value\> ',

                   '\</property\> ',

                   '',

                   '\</configuration\> '
                  ]
       cs = spb.getstatusoutput('cp /root/hdfs-site.xml /var/www/cgi-bin')
     
       for ins_ in hdfs_ins : 
          
            cs = spb.getstatusoutput('echo ' + ins_ + '>> hdfs-site.xml')
       
       putFiles('hdfs-site' , IP)


    else : 
       
       c_d = input('Do you want to change default replication factor and block size?[Y/N]')
       if c_d == 'Y' : 

          cs = spb.getstatusoutput(f'cp /root/hdfs-site.xml /var/www/cgi-bin')
          rp = int(input('Enter replication factor -> '))
          bs = int(input('Enter block size in bytes -> '))
          
          client_ins=['\<configuration\>' , '' , '\<property\>' , 
                      '\<name\>dfs.replication\</name\>' , f'\<value\>{rp}\</value\>','\</property\>' , '' , '\<property\>' ,  
                      '\<name\>dfs.block.size\</name\>' , f'\<value\>{bs}\</value\>','\</property\>' , '' , '\</configuration\>']

          for c_li in client_ins : 
                write = spb.getstatusoutput('echo ' + c_li + '>> hdfs-site.xml')
          

          putFiles('hdfs-site' , IP)

    #deleating and sending new files

    putFiles('core-site' , IP)

    print('core-site.xml and hdfs-site.xml configured successfully!')
  
     
    if mode == 'namenode' : 
           
           filestatus = spb.getstatusoutput(f'ssh {IP} mkdir /{filem_}')
           filestatus = print('Want to format[Y/N]?')
           filestatus = spb.getstatusoutput(f'ssh {IP} hadoop namenode -format')
    
    if mode in ('namenode' , 'datanode') : 

       runService = input('''
                          ---------------------------------------------
                          Do you want to start the service?[Y/N]
                          ---------------------------------------------
                          '''
                         )
    
       if runService == 'Y' :
   
            sc = spb.getstatusoutput(f'ssh {IP} hadoop-daemon.sh start {mode}')
            print(f'{mode} launched!' if sc[0] == 0 else 'Failed to launch!')
            sc = spb.getstatusoutput('ssh {IP} jps')

    else : print(f'{mode} launched!')       
   
################################################################################

IP = input("Enter the IP of remote system -> ")
conf = input("Configuration type -> ")

if conf.lower() == 'datanode' : 

    ip_master = input('Enter ip of master -> ')
    file_name = input('Enter your file name -> ')
    port = input('Enter service port number -> ')
    buildNode('datanode' , IP , port , ip_master , file_name , 'none')

elif conf.lower() == 'namenode':
    
    master_file_name = input('Enter your file name -> ')
    port = input('Enter service port number -> ')
    buildNode('namenode' , IP , port , 'none' , 'none' , master_file_name)    
 
elif conf.lower() == 'client':
    
    ip_master = input('Enter ip of master -> ')
    port = input('Enter ip of service port -> ')
    buildNode('client' , IP , port , ip_master , 'none' , 'none')  