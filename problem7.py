#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

from utilities import primes

N = int(1e4)
answer = next(itertools.islice(primes(), N, N + 1))

assert answer == 104743
print answer
