#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 整型（int）的常用方法演示

a = "123"
# int 将字符串转换为整型
b = int(a)
b = b + 100
print(b)

num = "0b11"
# 将字符串按照指定进制转换为数字
n1 = int(num,base = 2)
print(n1)

age = 19
# age的二进制的位数
length = age.bit_length()
print(length)