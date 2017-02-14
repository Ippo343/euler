#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import fibonacci

n_digits = 1000
M = 10**(n_digits - 1)

for i, f in enumerate(fibonacci()):
    if f >= M:
        break

# The +1 is necessary because we index from 0, math starts from 1
print i + 1
