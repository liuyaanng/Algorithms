#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

start = input("start: ")
stop = input("stop: ")
length = input("length: ")

def random_int_list(start, stop, length):
    """TODO: Docstring for random_int_list.
    :returns: TODO

    """
    start, stop, length = int(start), int(stop), int(length)
    if start <= stop:
        random_list = []
        for i in range(length):
            random_list.append(random.randint(start, stop))
    return random_list

def INSERTION_SORT_IN():
    """TODO: Docstring for INSERTION_SORT.
    :returns: TODO

    """
    test_arrays = random_int_list(start, stop, length)
    print(test_arrays)
    j = 2
    for j in range(len(test_arrays)):
        key = test_arrays[j]

        i = j - 1

        while i >= 0 and test_arrays[i] > key:
            test_arrays[i+1] = test_arrays[i]
            i = i - 1
        test_arrays[i+1] = key

    print(test_arrays)


def INSERTION_SORT_NE():
    """TODO: Docstring for INSERTION_SORT.
    :returns: TODO

    """
    test_arrays = random_int_list(start, stop, length)
    print(test_arrays)
    j = 2
    for j in range(len(test_arrays)):
        key = test_arrays[j]

        i = j - 1

        while i >= 0 and test_arrays[i] < key:
            test_arrays[i+1] = test_arrays[i]
            i = i - 1
        test_arrays[i+1] = key

    print(test_arrays)
INSERTION_SORT_IN()
INSERTION_SORT_NE()
