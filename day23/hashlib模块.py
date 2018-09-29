#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# hashlib模块
import hashlib

# md5加密的方法和过程
obj = hashlib.md5()
obj.update("hello".encode("utf8"))
print(obj.hexdigest())

# sha256加密的方法和过
obj2 = hashlib.sha256()
obj2.update("hello".encode("utf8"))
print(obj2.hexdigest())
