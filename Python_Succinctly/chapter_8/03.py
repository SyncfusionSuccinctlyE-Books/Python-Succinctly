#!/usr/bin/env python3

hosts = open('/etc/hosts')
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

hosts.seek(0)
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
