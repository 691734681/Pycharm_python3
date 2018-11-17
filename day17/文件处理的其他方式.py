#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 使用with方式操作文件则不需要自己手动关闭文件
# 使用with方式操作文件还可以一次打开多个文件
with open('xxx') as f,open('xxx2') as f2:
	data = f.read()
	print(data)
	data2 = f2.read()
	print(data2)


