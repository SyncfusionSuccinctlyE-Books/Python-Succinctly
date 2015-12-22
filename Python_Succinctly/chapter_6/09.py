#!/usr/bin/env python3

contacts = {
    'David': '555-0123',
    'Tom': '555-5678'
}
for contact in contacts:
    print('The number for {0} is {1}.'.format(contact, contacts[contact]))
