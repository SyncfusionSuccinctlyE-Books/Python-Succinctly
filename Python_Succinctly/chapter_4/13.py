#!/usr/bin/env python3


def get_name():
    """Get and return a name"""
    name = input('What is your name? ')
    return name


def say_name(name):
    """Say a name"""
    print('Your name is {}.'.format(name))


def get_and_say_name():
    """Get and display name"""
    name = get_name()
    say_name(name)

get_and_say_name()
