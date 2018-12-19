#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 追加模式，将要写的文件添加到存在文件的末尾
f = open('xxx2','a',encoding = 'utf-8')

print(f.readable())
print(f.writable())

f.write('算法\n')

f.close()