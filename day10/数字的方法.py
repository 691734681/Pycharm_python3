#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

#  将字符串转换成数字
s = "123"
n = int(s)
print(n)

# 将数字变为不同进制的数
s = "0011"
n = int(s,base = 2)
print(n)
n = int(s,base = 16)
print(n)

# 显示数字二进制的位数
n = 8
print(n.bit_length())