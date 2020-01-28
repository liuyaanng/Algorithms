#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random_list import random_int_list


def INSERTION_SORT_IN(sort):
    """TODO: SORT array by increasing.
    :returns: sorted

    """
    count = len(sort)
    for loop_index in range(2, count):
        insertion_index = loop_index - 1
        key = sort[loop_index]
        print(loop_index)
        while insertion_index >= 0 and sort[insertion_index] > key:
            sort[insertion_index + 1] = sort[insertion_index]
            insertion_index = insertion_index - 1
        sort[insertion_index + 1] = key

    return sort

def INSERTION_SORT_NE(sort):
    """TODO: SORT array by increasing.
    :returns: sorted

    """
    count = len(sort)
    for loop_index in range(2, count):
        insertion_index = loop_index - 1
        key = sort[loop_index]
        while insertion_index >= 0 and sort[insertion_index] < key:
            sort[insertion_index + 1] = sort[insertion_index]
            insertion_index -= 1
        sort[insertion_index + 1] = key

    return sort
