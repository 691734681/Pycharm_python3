#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from functools import reduce

# reduce函数
num = [1, 2, 3, 4, 100]

#
res = reduce(lambda x, y: x * y, num, 1)
print(res)
res = reduce(lambda x, y: x * y, num)
print(res)


