#!/usr/bin/env python3


def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)

lucky_numbers = [37, 71, 47, 13, 17, 67]
(highest, lowest) = high_and_low(lucky_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is: {}'.format(lowest))
