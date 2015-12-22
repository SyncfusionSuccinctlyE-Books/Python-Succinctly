#!/usr/bin/env python3

months_of_the_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
jan = months_of_the_year[0]
print(jan)
print()

for month in months_of_the_year:
    print(month)

# You cannot modify values in a tuple.  This will raise an exception.
months_of_the_year[0] = 'New January'
