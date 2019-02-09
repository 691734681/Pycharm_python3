#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 2,5,6,8,10,12,22,23  ###  7,8,9,10,11,19,22,25   ###   2,5,6,7,8,9,10,11,12,19,22,23,25

import random
l1 = [2,5,6,8,10,12,22,23]
l2 = [7,8,9,10,11,19,22,25]
l3 = [2,5,6,7,8,9,10,11,12,19,22,23,25]

def getBonus(l):
    """bonus"""
    red = random.sample(l,6)
    red.sort()
    blue = random.sample(l[0:-3],2)
    blue.sort()
    return red,blue

print(getBonus(l1))
print(getBonus(l2))

def getBonus2(l,i,j):
    """bonus"""
    red = random.sample(l,i)
    red.sort()
    blue = random.sample(l[0:9],j)
    blue.sort()
    return red,blue

print(getBonus2(l3,7,2))
print(getBonus2(l3,7,3))









