#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

def to_str(num, base):
    convert = '0123456789ABCDEF'
    if num < base:
        return convert[num]
    else:
        return to_str(int(num/base), base) + convert[num % base]

res = to_str(11,2)
print(res)


