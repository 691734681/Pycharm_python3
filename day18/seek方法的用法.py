#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 读取log.txt文件的最后一行

"""
方法一:使用readlines()，读取所有，以列表形式存放，然后取出最后一行，
这样做一次性读取所有内容，如果文件大会很占内存
"""
"""
f = open('log.txt',encoding = 'utf8')
data = f.readlines()
print(data[-1])
f.close()
"""

"""
方法二：直接遍历f句柄，使用seek方法从后往前读，这样比较节省内存
"""
f = open('log.txt','rb')
offset = -6 # 因为不知道最后一行有多少字节，先设定为6，符号表示从后往前数
while True:
	f.seek(offset,2) # 2表示从最后往前数
	data = f.readlines() # readlines() 是将读取到的内容以行为单位存放的列表中
	if len(data) > 1: # 表示读取到不止一行
		print(data[-1].decode('utf8')) #直接将最后一行读取并退出
		break
	offset *= 2
