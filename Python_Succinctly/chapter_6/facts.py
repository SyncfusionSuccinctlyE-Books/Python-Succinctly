#!/usr/bin/env python3


def display_facts(facts):
    """Displays facts"""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()

facts = {
    'David': 'Was a mascot in college.',
    'Jeff':  'Was born in France.',
    'Anna': 'Has arachnophobia.'
}

display_facts(facts)

facts['David'] = 'Can juggle.'
facts['Dylan'] = 'Has a pet hedgehog.'

display_facts(facts)
