#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random_list import random_int_list

def add_binary():
    """TODO: Docstring for add_binary.
    :returns: TODO

    """
    A = random_int_list(0, 1, 10)
    B = random_int_list(0, 1, 10)
    C =[]
    print("A = ", A)
    print("B = ", B)
    A.append(0)
    B.append(0)
    for i in range(len(A)):
        key = A[i] + B[i]
        if key == 0 or key == 1:
            C.append(key)
        elif key == 2:
            C.append(0)
            A[i + 1] += 1
        else:
            C.append(1)
            A[i + 1] += 1
    print("C = ", C)


add_binary()
