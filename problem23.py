#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown 
that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known 

that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import utilities

smallest_abn = 12
upper_limit = 28123

cache = {n: (n == smallest_abn) for n in xrange(smallest_abn + 1)}


def is_abundant(n):
    try:
        return cache[n]
    except KeyError:
        retval = (sum(utilities.divisors(n, only_proper=True)) > n)
        cache[n] = retval
        return retval


def is_sum_of_abundants(n):
    for a in xrange(smallest_abn, (n + 1)):
        if not is_abundant(a):
            continue
        elif is_abundant(n - a):
            return True
    else:
        return False


if __name__ == '__main__':
    numbers = xrange(upper_limit + 1)
    print sum(n for n in numbers if not is_sum_of_abundants(n))
