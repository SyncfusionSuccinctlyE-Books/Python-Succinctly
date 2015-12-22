#!/usr/bin/env python3

# Open a file and assign its contents to a variable.
# If the file is unavailable, create an empty variable.
try:
    contacts = open('contacts.txt').read()
except:
    contacts = []

print(len(contacts))
