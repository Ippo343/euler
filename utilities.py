#!/usr/bin/env python

import itertools

import math


def lower_than(n):
    return lambda x: x < n


def le_than(n):
    return lambda x: x <= n


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    sieve = {}

    for n in itertools.count(start=2):
        if n not in sieve:
            # n is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield n
            sieve[n * n] = [n]
        else:
            # n is composite. sieve[n] is the list of primes that
            # divide it. Since we've reached n, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in sieve[n]:
                sieve.setdefault(n + p, []).append(p)
            del sieve[n]


class PrimeCache(object):
    def __init__(self):
        super(PrimeCache, self).__init__()
        self._cache = {1}
        self._generator = primes()
        self._max = 0

    def is_prime(self, n):
        while self._max < n:
            nxt = next(self._generator)
            self._cache.add(nxt)
            self._max = max(self._max, nxt)
        return n in self._cache


def divisors(n, only_primes=False, only_proper=False):
    limit = int(math.floor(math.sqrt(n)))

    candidates = primes() if only_primes else itertools.count(start=1)
    candidates = itertools.takewhile(le_than(limit), candidates)

    for c in candidates:

        if not n % c:
            # Found a divisor
            yield c

            # Now also yield its "mirror" (i.e, m: m*c = n with m > sqrt(n))
            m = (n / c)
            if (m == c) or (only_proper and m == n):
                continue
            else:
                yield m
