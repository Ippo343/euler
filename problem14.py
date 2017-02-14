#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import lower_than
from itertools import count, imap, takewhile

from functools import lru_cache

limit = 1e6


@lru_cache
def collatz_len(n):

    if n == 1:
        return 1
    else:
        return 1 + collatz_len((3*n + 1) if (n % 2) else (n / 2))


answer = max(imap(collatz_len, takewhile(lower_than(limit), count(start=1))), key=lambda t: t[1])
print(answer)
