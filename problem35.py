#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from collections import deque

import utilities

pc = utilities.PrimeCache()


def rotate(s, n):
    d = deque(s)
    d.rotate(n)
    return ''.join(d)


def rotations(s):
    for n in xrange(len(s)):
        yield rotate(s, n)


def is_circular_prime(n):
    retval = all(pc.is_prime(int(r)) for r in rotations(str(n)))
    return retval


if __name__ == '__main__':
    count = 0
    for n in xrange(2, int(1e6)):
        if is_circular_prime(n):
            count += 1
    print count
