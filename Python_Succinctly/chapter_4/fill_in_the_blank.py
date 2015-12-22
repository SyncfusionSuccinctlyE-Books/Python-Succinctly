#!/usr/bin/env python3


def get_word(word_class):
    """Get a word from a standard input and return that word."""
    if word_class.lower() == 'adjective':
        article = 'an'
    else:
        article = 'a'
    return input('Enter a word that is {0} {1}: '.format(article, word_class))


def fill_in_the_blanks(noun, verb, adjective):
    """Fills in the blanks and returns a completed story."""
    story = "I never knew anyone that hadn't {1} at least once in their life, except for {2}, old Aunt Polly. She never {1}, not even when that {0} came to town.".format(noun, verb, adjective)
    return story


def print_story(story):
    """Prints a story."""
    print()
    print('Here is the story you created.  Enjoy!')
    print()
    print(story)


def create_story():
    """Creates a story by collecting the input and printing a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    print_story(the_story)

create_story()
