#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine
the shortest possible secret passcode of unknown length.
"""

from collections import defaultdict


def pop_empty(dictionary):
    for k, v in dictionary.iteritems():
        if not v:
            del dictionary[k]
            return k
    else:
        raise ValueError(u"No empty key")


def remove_value(dictionary, value):
    for value_set in dictionary.itervalues():
        if value in value_set:
            value_set.remove(value)


if __name__ == '__main__':
    digits_preceding = defaultdict(set)

    with open('data/p079_keylog.txt') as f:
        for line in map(str.strip, f):
            for idx in xrange(len(line)):
                c = line[idx]
                digits_preceding[c].update(line[:idx])

    solution = ''

    while digits_preceding:
        first = pop_empty(digits_preceding)
        remove_value(digits_preceding, first)
        solution += first

    assert solution == '73162890'
    print solution
