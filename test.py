#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Sort
from random_list import random_int_list
start = time.perf_counter()

sort = random_int_list(0, 100, 10000)
print(sort)
#sorted = Sort.INSERTION_SORT_NE(sort)
sorted = Sort.SELECT_SORT(sort)
print(sorted)

elapsed = (time.perf_counter() - start)
print("Time used: ", elapsed)

