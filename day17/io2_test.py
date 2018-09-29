#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 文件的打开模式：只读(r)，写(w),追加(a)；默认的打开方式是只读
# f = open("test", "r")默认就是r，所以可以省略
f = open("test")
# data = f.read()
# 文件是否可读
print(f.readable())
# 文件是否可写
print(f.writable())
# 读一行
print(f.readline())
print("="*50)
print(f.readlines())
# print("=" * 50)
# data = f.read()
# print(data)
f.close()
