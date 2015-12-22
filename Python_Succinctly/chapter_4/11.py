#!/usr/bin/env python3


def even_or_odd(number):
    """Determine if a number is even or odd."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

even_or_odd_string = even_or_odd(9)
print(even_or_odd_string)
