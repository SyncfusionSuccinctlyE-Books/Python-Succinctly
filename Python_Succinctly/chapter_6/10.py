#!/usr/bin/env python3

contacts = {'David': '555-0123', 'Tom': '555-5678'}
for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))
