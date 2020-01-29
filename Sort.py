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

def MERGE_SORT(A, p, r):
    """TODO: Docstring for MERGE_SORT.

    :A: sort array
    :p: begin index
    :r: end index
    :returns: sorted

    """
    if p < r:
        q = (p + r) // 2
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q + 1, r)
        MERGE(A, p, q, r)
    return A

def MERGE(A, p, q, r):
    """TODO: Docstring for MERGE(A, p, q, r):.
    :returns: TODO
    """
    L_arr = A[p:q+1] + [float('inf')]
    R_arr = A[q+1:r+1] + [float('inf')]
    L_index, R_index = 0, 0
    for loop_index in range(p, r + 1):
        if L_arr[L_index] <= R_arr[R_index]:
            A[loop_index] = L_arr[L_index]
            L_index += 1
        else:
            A[loop_index] = R_arr[R_index]
            R_index += 1
    



