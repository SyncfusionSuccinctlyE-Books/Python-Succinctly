#!/usr/bin/env python3

# Ask for the distance.
distance = input('What distance are you traveling in miles? ')

# Convert the distance into an integer.
distance = int(distance)

# Determine what transportation to use.
if distance < 3:
    transportation = 'walking'
elif distance < 300:
    transportation = 'driving'
else:
    transportation = 'flying'

# Display the result.
print('I suggest {} to your destination.'.format(transportation))
