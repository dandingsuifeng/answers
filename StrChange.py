# -*- coding: utf-8 -*-

def normalize(n):
    n.capitalize()

L1 = ['adam','LISA','barT']
#L2 = list(map(normalize, L1))
L2 =[]
for x in L1:
    x.lower()
    x.capitalize()
    L2.append(x.capitalize())

print(L2)
#迷之输出none