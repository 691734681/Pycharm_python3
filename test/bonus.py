#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random

l = []
for i in range(6):
    t = random.randint(1,33)
    if len(l) != 6:
        l.append(t)

i = random.randint(1,16)

print(l)
l.sort()
print(l)
print(i)
