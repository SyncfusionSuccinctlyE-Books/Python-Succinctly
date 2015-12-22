#!/usr/bin/env python3

animals = ['toad', 'lion', 'seal', 'fox', 'owl', 'whale']

some_animals = animals[1:4]
print('Some animals:      {}'.format(some_animals))

first_two = animals[0:2]
print('First two animals: {}'.format(first_two))

first_two_again = animals[:2]
print('First two animals: {}'.format(first_two_again))

last_two = animals[4:6]
print('Last two animals:  {}'.format(last_two))

last_two_again = animals[-2:]
print('Last two animals:  {}'.format(last_two_again))
