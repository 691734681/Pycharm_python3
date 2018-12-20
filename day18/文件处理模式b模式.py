#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# b模式默认以字节方式操作

# 以字节模式读操作时，不能在open中指定字符编码
f_r = open('数据结构.txt','rb')
data = f_r.read()
print(data)
print(data.decode('utf-8'))
f_r.close()

# 以b模式写文件，需要将内容变成字节，而且需要指定编码方式
f_w = open('test2.txt','wb')
s = '你好\n'
s1 = '上海\n'
f_w.write(bytes(s,encoding = 'utf-8'))
f_w.write(s1.encode('utf8'))
f_w.close()

