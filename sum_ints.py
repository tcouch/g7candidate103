# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:43:09 2021

@author: Jim Tyson

Convert the following python function so that it can sum a
vector of integers.

"""


def sum_ints(*args):
    result = 0
    for arg in args:
        if isinstance(arg, list):
            result += sum_ints(*arg)
        else:
            result += arg
    return result

