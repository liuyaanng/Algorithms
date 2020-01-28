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

def SELECT_SORT(sort):
    """TODO: Docstring for SELECT_SORT.

    :sort: TODO
    :returns: TODO

    """
    count = len(sort)
    for loop_index in range(count):
        key = sort[loop_index]
        for select_index in range(loop_index, count - 1):
            if key > sort[select_index]:
                key = sort[select_index]
                index = select_index
        sort[loop_index], sort[index] = sort[index], sort[loop_index]
    #print("sort index is ", index)
    #print("min is ", min)

    return sort

