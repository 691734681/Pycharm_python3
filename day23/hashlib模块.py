#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# hashlib用于对字符串加密

import hashlib

"""
# 这样加密如果是比较简单的字符串可以通过反向解密破解
obj = hashlib.md5() # 获取Md5对象
obj.update('admin'.encode('utf8'))  # 将要加密的字符变成指定编码的字节
s = obj.hexdigest() # 获取加密后的字符串
print(s)
"""

"""
obj = hashlib.md5('test'.encode('utf8'))  # 在获取md5对象时就添加一个字符串，就无法反向解密
obj.update('admin'.encode('utf8'))
s = obj.hexdigest()
print(s)
"""

obj = hashlib.md5()
obj.update('admin'.encode('utf8'))
s1 = obj.hexdigest()
print(s1)

obj.update('root'.encode('utf8'))   # 这里的root加密是在admin的基础上，相当于一个新的obj.update('adminroot'.encode('utf8))
s2 = obj.hexdigest()
print(s2)

obj2 = hashlib.md5()
obj2.update('adminroot'.encode('utf8'))
s3 = obj2.hexdigest()     # s2 和 s3输出相同
print(s3)