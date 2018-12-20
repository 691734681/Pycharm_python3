#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# num是要转的数，base是要转的进制，使用的是递归算法
"""
递归算法的三大定律：
1.递归算法必须有个基本的结束条件
2.递归算法必须改自己的状态并向基本结束条件演进
3.递归算法必须调用自身
"""
def to_str(num, base):
    convert = '0123456789ABCDEF'
    if num < base:
        return convert[num]
    else:
        return to_str(int(num/base), base) + convert[num % base]

res = to_str(11,2)
print(res)