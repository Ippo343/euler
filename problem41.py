"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utilities import divisors
from itertools import permutations


def largest_pandigital_prime(n):
    digits = sorted(xrange(1, n + 1), reverse=True)
    for comb in permutations(digits):

        if comb[-1] in (0, 2, 4, 5, 6, 8):
            # Even numbers and multiples of 5 are obviously not prime
            continue

        num = int(''.join(str(d) for d in comb))
        if any(divisors(num, only_primes=True, only_proper=True)):
            continue
        else:
            return num
    else:
        return None


if __name__ == '__main__':

    # The solution can't have 5, 6, 8 or 9 digits because:
    # sum(1..9) = 45
    # sum(1..8) = 36
    # sum(1..6) = 21
    # sum(1..5) = 15
    # So every pandigital number with that number of digits is divisible by 3
    # The problem text tells you that 2143 is prime, therefore the solution must be at least 4 digits long
    # and this rules out 3 too.
    candidate_n = [7, 4]

    for n in candidate_n:
        p = largest_pandigital_prime(n)
        if p:
            assert p == 7652413
            print p
            break
