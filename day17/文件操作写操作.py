#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 写操作,w模式会没有文件创建文件，有文件覆盖原文件
f = open('xxx2','w',encoding = 'utf-8')

# 是否可读
print(f.readable())
# 是否可写
print(f.writable())

# 写入内容
f.write('1111111111\n')
f.write('2222222222\n')
f.write('333\n4444\n5555\n')

# writelines()参数是列表，将列表内容写入
l = ['abcd\n','efgh\n','ijk\n']
f.writelines(l)

# 关闭文件
f.close()


