#!/usr/bin/env python3

contacts = {
    'David': ['555-0123', '555-0000'],
    'Tom': '555-5678'
}

if 'David' in contacts:
    print("David's phone number is:")
    print(contacts['David'][0])

if 'Nora' in contacts:
    print("Nora's phone number is:")
    print(contacts['Nora'][0])
