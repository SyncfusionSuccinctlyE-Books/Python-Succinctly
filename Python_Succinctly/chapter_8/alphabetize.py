#!/usr/bin/env python3

unsorted_file_name = 'animals.txt'
sorted_file_name = 'animals-sorted.txt'
animals = []

try:
    with open(unsorted_file_name) as animals_file:
        for line in animals_file:
            animals.append(line)
    animals.sort()
except:
    print('Could not open {}.'.format(unsorted_file_name))

try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))
