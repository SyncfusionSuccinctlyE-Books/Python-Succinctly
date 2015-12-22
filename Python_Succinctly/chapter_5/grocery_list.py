#!/usr/bin/env python3

# Create a list to hold the grocery items.
grocery_list = []
finished = False
while not finished:
    item = input('Enter an item for your grocery list.  Press <ENTER> when done: ')
    if len(item) == 0:
        finished = True
    else:
        grocery_list.append(item)
        print('Item added.')

# Display the grocery list.
print()
print('Your Grocery List:')
print('-' * 18)
for item in grocery_list:
    print(item)
