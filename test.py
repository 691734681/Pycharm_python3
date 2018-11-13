#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

name = 'alex'
def foo():
	name = 'linhaifeng'
	def bar():
		print(name)
	return bar

res = foo()
print(res)
