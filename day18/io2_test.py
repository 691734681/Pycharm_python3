#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

#
f = open("test", "r+", encoding="utf-8")
print(f.encoding)
data = f.read()
print(data)
print(f.tell())
# 截取指定长度的字符(按字节数截取)(从头开始截取)
f.truncate(10)
f.close()
