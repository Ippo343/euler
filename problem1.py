"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Answer:
    233168
"""


import itertools
from utilities import lower_than


LIMIT=1000
ANSWER=233168


def multiples(n):
    """
    Yields all the multiples of n (to infinity)
    """
    for i in itertools.count(start=1):
        yield i*n

threes = itertools.takewhile(lower_than(LIMIT), multiples(3))
fives = itertools.takewhile(lower_than(LIMIT), multiples(5))

# It's important to have a set here as there are numbers that are divisible by both 3 and 5
# If you don't use a set these numbers are counted twice and the answer is not correct
answer = sum(set(itertools.chain(threes, fives)))
assert answer == ANSWER

print answer

