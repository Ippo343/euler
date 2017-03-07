#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import math

from utilities import lower_than

N = 1000


def is_perfect_square(n):
    s = math.sqrt(n)
    return s == int(s)


def find_tuple():
    for a in itertools.takewhile(lower_than(N - 1), itertools.count(1)):
        for b in itertools.takewhile(lower_than(N - a), itertools.count(a + 1)):
            c = math.sqrt(a * a + b * b)
            if a + b + c == N:
                return a, b, int(c)
    else:
        raise ArithmeticError("Not found!")


a, b, c = find_tuple()

assert a * a + b * b == c * c
assert a + b + c == N

print a, b, c

assert a * b * c == 31875000
print a * b * c
