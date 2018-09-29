#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 内置函数map
num_l = [1, 2, 10, 5, 3, 7]

# 实现列表中每个数字的平方
# map函数中第一参数是实现功能的函数，第二个参数是一个可以迭代的对象
# 返回的结果是个迭代器，迭代器的特点是只能迭代一次
res = map(lambda x: x + 1, num_l)
print(res)
print(type(res))
l_l = list(res)
# 这次再使用list打印迭代器就是个空的列表
print(list(res))
print(l_l)
print(l_l)

