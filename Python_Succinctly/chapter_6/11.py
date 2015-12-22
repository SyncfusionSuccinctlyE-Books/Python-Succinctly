#!/usr/bin/env python3

contacts = {
    'David': {
        'phone': '555-0123',
        'email': 'david@gmail.com'
    },
    'Tom': {
        'phone': '555-5678',
        'email': 'tom@gmail.com'
    }
}

for contact in contacts:
    print("{}'s contact info:".format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])
