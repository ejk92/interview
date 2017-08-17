# -*- coding: utf-8 -*-

from operator import mul


def calculate_highest_product(numbers):
    """
    Generate highest product of 3 numbers from list.
    Steps:
    0. return False if length of list is fewer than 3
    1. Sort numbers descanding
    2. Multiply the first three numbers from list
    """
    if len(numbers) < 3:  # Length of list must be greater than 2
        return False
    return reduce(mul, sorted(numbers, reverse=True)[:3])


if __name__ == '__main__':

    test_cases = [
    ([1, 2, 3, 5, 4], 60),
    ([1, 10, 2, 6, 5, 3], 300),
    ([5, 7, 0, 0, 1], 35),
    ([0, 2], False)
    ]

    for numbers, output in test_cases:
        print '{}, test case output: {}, from function: {}'.format(numbers, output, calculate_highest_product(numbers))
