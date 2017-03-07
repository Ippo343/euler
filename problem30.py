#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def sum_fifth_powers(number):
    """ Awkward and C-think, but fast """
    s = 0
    while number:
        number, digit = number // 10, number % 10
        s += (digit ** 5)

    return s


if __name__ == '__main__':

    max_num = int(6 * 9 ** 5)

    solutions = set()
    for n in xrange(2, max_num):
        s = sum_fifth_powers(n)
        if n == s:
            solutions.add(n)

    print solutions
    answer = sum(solutions)

    assert answer == 443839
    print answer
