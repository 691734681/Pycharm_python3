#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 解压序列
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2]

# 取l第一个和最后一个值，不使用角标
# *x表示将序列中间的部分作为列表赋值给x
a, *x, b = l
print("%s,%s" % (a,b))
print(x)

A,B = l2
print(A,B)

# 交换A,B的值
A,B = B,A
print(A,B)

