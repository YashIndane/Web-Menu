#!/usr/bin/python3

from subprocess import getstatusoutput as gso

print('content-type:text/plain')
print()

x=gso('sudo /usr/local/bin/ansible-playbook /ansible-scripts/elastic_cache.yml')
print(x)


