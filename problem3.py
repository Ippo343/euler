#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import itertools
import math

from utilities import primes, lower_than

number = 600851475143
limit = int(math.floor(math.sqrt(number)))

answer = 1
for p in itertools.takewhile(lower_than(limit), primes()):
    if not number % p:
        answer = p

assert answer == 6857
print answer
