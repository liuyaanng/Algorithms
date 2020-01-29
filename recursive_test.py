#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum(n):
    """TODO: Docstring for sum.

    :n: TODO
    :returns: TODO

    """
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


res = sum(100)
print(res)
