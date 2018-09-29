#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 追加模式(a)
# a：如果文件有内容，在文件最后添加新内容
f = open("test", "a")
f.write("888888\n")
print(f.readable())
f.close()

