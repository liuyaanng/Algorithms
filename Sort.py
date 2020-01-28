#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random_list import random_int_list

start = input("start: ")
stop = input("stop: ")
length = input("length: ")

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
