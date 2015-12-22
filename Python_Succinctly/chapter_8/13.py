#!/usr/bin/env python3

with open('pig.jpg', 'rb') as pig_picture:
    pig_picture.seek(2)
    pig_picture.read(4)
    print(pig_picture.tell())
    print(pig_picture.mode)
