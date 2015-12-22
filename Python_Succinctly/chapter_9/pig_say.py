#!/usr/bin/env python3


def pig_say(text):
    """Generate a picture of a pig saying something"""
    text_length = len(text)
    print('              {}'.format('_' * text_length))
    print('            < {} >'.format(text))
    print('              {}'.format('-' * text_length))
    print('            /')
    print('     ^..^  /')
    print('~(  ( oo )')
    print('  ,,  ,,')


def main():
    text = input('What would you like the pig to say? ')
    pig_say(text)

if __name__ == '__main__':
    main()
