#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sort
from random_list import random_int_list

sort = random_int_list(0, 100, 20)
print(sort)
sorted = Sort.INSERTION_SORT_NE(sort)
print(sorted)

