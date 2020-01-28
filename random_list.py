#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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
