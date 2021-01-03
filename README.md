![](https://img.shields.io/badge/license-MIT-yellow) ![](https://img.shields.io/badge/python-3.8-brightgreen)
# Web-Menu
A Webapp that is hosted on a Apache HTTPD server and gives functionality to automate Hadoop-clustering , Docker configuration and automating AWS services. Commands can be spoken or typed in the specific fields. For some commands Ansible has been used.
It provides facility of Logical Volume Management (LVM) for providing elasticity to datanodes.

![](Images/web2.png)

After configuring the httpd server just run - 
```
bash start.sh
```
# Configuring Apache httpd server

The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server software, released under the terms of Apache License 2.0. 

## Installation (RHEL7 and above)

The following commands are for installing httpd , checking status of httpd , to enable httpd ,to start the server and to stop the server respectively. 
```
yum install httpd 

systemctl status httpd
systemctl enable htpd
systemctl start httpd   
systemctl stop httpd
```

As the automation program is a long process , so the server will throw **Gateway Timeout error** . Just add the line `TimeOut 6000` anywhere in the hadoop configuration file ie. ,
`etc/hadoop/conf/hadoop.conf`

## Hadoop Automation

Apache Hadoop is a collection of open-source software utilities that facilitates using a network of many computers to solve problems involving massive amounts of data and computation. It provides a software framework for distributed storage and processing of big data using the MapReduce programming model.
Hadoop requires jdk 
The webapp installs jdk and hadoop by - 

```
sudo /usr/local/bin/ansible all -m command -a"rpm -i jdk-8u171-linux-x64.rpm"
sudo /usr/local/bin/ansible all -m command -a"rpm -i hadoop-1.2.1-1.x86_64.rpm --force"
```

By default apache does not have permission for writing to a file. In that case make apache owner of that file-

```chown apache file_path```

## Logical Volume Management (LVM)

This concept is very helpful in scenarios where dynamic rezising of volume is required. Volume can be incresed or decresed on the fly. Steps that Web-Menu uses to do this is.
![](Images/vl.png)

## Automating AWS Services

Amazon Web Services is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

## Installing aws-cli 

for Linux x86(64-bit)

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
For more details and for getting specific version refer to - [AWS Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html):page_facing_up:

for using any of the functionality, login inside your account using IAM user id and key 

```
aws configure
```
This web-app can start and stop EC2 instance , create security groups , create S3 bucket and create distribution for using CDN.

![](Images/1.png)

Example lets's create a S3 bucket for object type storage-

![](Images/4.png) ![](Images/3.png)

![](Images/78.png)

## AWS VPC

Amazon Virtual Private Cloud (Amazon VPC) is a service that lets you launch AWS resources in a logically isolated virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.

## AWS HAProxy load balancing

HAProxy is free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers.

This is done with the help of Ansible playbooks. 
Installing Ansible -

```
pip3 install ansible
````
but for Ansible to work with ssh , we need to install sshpass, and for this we download the already available yum configuration file-

```
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

Now install sshpass by
```
yum install sshpass
```

mention `privilege escalation` properties inside `/etc/ansible/ansible.cfg`

For getting information on various Ansible modules used inside `Web Menu` , see here ->  [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html) 

## Docker automation

Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

## Installing docker

open the file **/etc/yum.repos.d** , make a new file with extension **.repo** and configure the file as-

```
[tag_name]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
```
Install by-

```
yum install docker-ce --nobest
```
for getting information about available containers for docker visit [Docker Hub](https://hub.docker.com/search?q=&type=image):whale:

![](Images/66.png)

![](Images/1.jpg)

## NFS

Network File System is a distributed file system protocol originally developed by Sun Microsystems in 1984, allowing a user on a client computer to access files over a computer network much like local storage is accessed.

The main configuration file is `/etc/exports`.  By default the user only has `read-access` to the file , For giving `read-write access` ->

```
<file-path> <ip> (rw,no_root_squash)
```

To access the folder it first has to be mounted. Web-Menu uses Ansible ad-hoc command to mount the folder->

```sudo /usr/local/bin/ansible <ip> -m mount -a"src=<remote_ip>:/<folder path=<mount_point fstype=nfs state=mounted>```
































