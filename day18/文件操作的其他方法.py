#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

#
f = open('数据结构.txt','r+',encoding = 'utf8')

# flush() 刷新缓存区
#f.flush()

# name 文件名
#print(f.name)

# tell()：当前光标所在位置,是按字节算的
print(f.tell())
f.readline()
f.readline()
data = f.read(1) # read()是按字符算的
print(data)
print(f.tell())

# seek():控制光标的位置,是按照字节算的
f.seek(1)
print(f.tell())

# truncate():文件截断
# 从位置0截取指定长度的内容:长度按字节算
print(f.truncate(10))

f.close()