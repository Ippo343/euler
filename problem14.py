#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import count, takewhile

from utilities import lower_than

limit = 1e6

cache = {1: 1}


def collatz_len(n):
    try:
        return cache[n]
    except KeyError:
        retval = 1 + collatz_len((3 * n + 1) if (n % 2) else (n / 2))
        cache[n] = retval
        return retval


gen = ((n, collatz_len(n)) for n in takewhile(lower_than(limit), count(1)))
answer = max(gen, key=lambda t: t[1])[0]
assert answer == 837799

print answer
