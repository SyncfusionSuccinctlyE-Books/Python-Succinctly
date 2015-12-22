#!/usr/bin/env python3

cities = [
    ('Short Hills, NJ', '07078'),
    ('Fairfax Station, VA', '22039'),
    ('Weston, CT', '06883'),
    ('Great Falls, VA', '22066')
]

for (city, zip_code) in cities:
    print('The zip code for {} is {}.'.format(city, zip_code))
