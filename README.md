![](https://img.shields.io/badge/license-MIT-yellow) ![](https://img.shields.io/badge/python-3.8-brightgreen)
# Web-Menu
A Webapp that is hosted on a Apache HTTPD server and gives functionality to automate Hadoop-clustering , Docker configuration and AWS. Commands can be spoken or typed in the specific fields. For some commands Ansible has been used.
It provides facility of Logical Volume Management (LVM) for providing elasticity to datanodes.

![](Images/layout2.jpg)

# Configuring Apache httpd server

The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server software, released under the terms of Apache License 2.0. 

## Installation (RHEL7 and above)
```
yum install httpd
```
To check status of httpd
```
systemctl status httpd
```
To enable httpd (i.e to start it on every boot)
```
systemctl enable httpd
```
