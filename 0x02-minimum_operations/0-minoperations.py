#!/usr/bin/python3
""" Gets the minimum operations """


def minOperations(n):
    """ calculates the fewest number of operations
    needed to result in n H charaters """
    if n  0:
        return 0
    operations = 0
    i = 1
    while i < n:
        i *= 2
        operations += 1
    return operations
