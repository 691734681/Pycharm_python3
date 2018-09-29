#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from functools import reduce

# 将序列中的数字变成字符
l = [1, 2, 3, 4, 5]
l2 = map(str, l)
print(list(l2))

# 求序列 l 中的数字的和
res = reduce(lambda x, y: x + y, l)
print(res)

# 过滤sb
name = ["alex_sb", "linhaifeng"]
new_name = filter(lambda s: not s.endswith("sb"), name)
print(list(new_name))
