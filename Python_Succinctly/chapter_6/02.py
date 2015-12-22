#!/usr/bin/env python3

contacts = {'David': '555-0123', 'Tom': '555-5678'}
contacts['David'] = '555-0000'
davids_phone = contacts['David']
print('Dial {} to call David.'.format(davids_phone))
