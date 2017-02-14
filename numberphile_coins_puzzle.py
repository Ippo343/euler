#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import random
from collections import deque

H = True
T = False
HT = (H, T)


def _to_letters(seq):
    return ''.join("H" if s else "T" for s in seq)


def counter_seq(seq):
    """
    Returns the counter-sequence for the given sequence
    """
    assert len(seq) == 3
    return not seq[1], seq[0], seq[1]


def play_match(seqA, seqB):
    """
    Plays a single match between two sequences.
    Returns the winner.
    """
    seq = deque(maxlen=3)

    for _ in xrange(3):
        seq.append(random.choice(HT))

    while True:
        lseq = tuple(seq)
        if seqA == lseq: return seqA
        if seqB == lseq: return seqB

        seq.append(random.choice(HT))


def evaluate_prob(seqA, seqB, N=10000):
    """
    Plays N matches between the two sequencies returning the total amount of won rounds
    """
    victories = {seqA: 0, seqB: 0}
    for _ in xrange(N):
        winner = play_match(seqA, seqB)
        victories[winner] += 1

    return victories


all_starts = itertools.product(HT, repeat=3)
counters = {s: counter_seq(s) for s in all_starts}


if __name__ == '__main__':

    N = int(1e6)
    for expected_loser, expected_winner in counters.iteritems():

        victories = evaluate_prob(expected_loser, expected_winner, N)
        prob = float(victories[expected_winner]) / N

        print "{} lost to {} {}% of the time".format(
            _to_letters(expected_loser),
            _to_letters(expected_winner),
            prob * 100)
