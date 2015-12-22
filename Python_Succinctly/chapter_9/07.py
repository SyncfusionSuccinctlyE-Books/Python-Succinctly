#!/usr/bin/env python3

import sys
file_name = 'test.txt'
try:
    with open(file_name) as test_file:
       for line in test_file:
           print(line)
except:
    print('Could not open {}.'.format(file_name))
    sys.exit(1)
