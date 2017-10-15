# -*- coding: utf-8 -*-
from functools import reduce


def prod(L):
    def Multiply(a,b):
        return a*b
    return reduce(Multiply,L)


print(prod([3, 5, 7, 9]))