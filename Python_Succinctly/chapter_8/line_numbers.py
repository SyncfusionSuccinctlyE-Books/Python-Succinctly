#!/usr/bin/env python3

with open('file.txt') as file:
    line_number = 1
    for line in file:
        print('{}: {}'.format(line_number, line.rstrip()))
        line_number += 1
