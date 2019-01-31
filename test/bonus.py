#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random
l = []
while True:
    if len(l) == 6:
        break
    t = random.randint(1,34)
    if t in l:
        continue
    else:
        l.append(t)
l.sort()
l.append(random.randint(1,17))
print(l)

