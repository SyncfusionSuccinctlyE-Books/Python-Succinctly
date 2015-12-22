#!/usr/bin/env python3

animals = ['toad', 'lion', 'seal']
try:
    sheep_index = animals.index('sheep')
except:
    sheep_index = 'No sheep found.'
print(sheep_index)
