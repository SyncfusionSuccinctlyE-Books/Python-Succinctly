#!/usr/bin/env python3

hosts = open('/etc/hosts')
hosts_file_contents = hosts.read()
print(hosts_file_contents)
hosts.close()
