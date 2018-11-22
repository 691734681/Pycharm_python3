#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 函数嵌套 : 在函数中定义了另一个函数

def father(name):
	print('from father %s' % name)
	def son():
		print('from son')
		def grandson():
			print('from grandson')
		grandson()
	son()

father('林海峰')