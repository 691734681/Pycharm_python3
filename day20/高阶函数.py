#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time


# 高阶函数：函数参数接收的是一个函数名或函数的返回值是一个函数名


def foo():
	"""desc"""
	print("你好啊")


# test接收的参数是个函数，所以是高阶函数
def test(func):
	"""desc"""
	print(func)
	func()


test(foo)

print("=" * 50)


# test2返回的是个函数名，所以是高阶函数
def foo2():
	"""desc"""
	print("from the foo2")


def test2(func):
	"""desc"""
	return func


print(test2(foo2))
res = test2(foo2)
res()






