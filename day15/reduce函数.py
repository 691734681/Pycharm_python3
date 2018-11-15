#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
reduce函数的使用:
格式:reduce(func,list_num)
func:是一个函数，如果函数结构简单可以用lambda
list_num:是一个可迭代序列
作用：是通过func函数处理可迭代序列中的每个值
返回：返回的是一个可迭代序列
"""

from functools import reduce

# 求列表中所数字的和
num_l = [1,2,3,4,5,6,7,8,9,10]

res = reduce(lambda x, y : x + y, num_l)
print(res)

