#!/usr/bin/env python3

months_of_the_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(months_of_the_year)
del months_of_the_year
# This will raise an exception since the tuple was deleted.
print(months_of_the_year)
