#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time

# 高阶函数：函数接收的参数是个函数或者返回值是个函数

def foo():
	time.sleep(5)
	print('foo')


# 实现高阶函数方式一：函数接收一个函数做参数
# def 数据结构(func):
# 	start_time = time.time()
# 	func()
# 	stop_time = time.time()
# 	print('time is %s ' % (stop_time - start_time))
#
# 数据结构(foo)

# 实现高阶函数方式二：返回值是一个参数
def test(func):
	start_time = time.time()
	func()
	stop_time = time.time()
	print('time is %s ' % (stop_time - start_time))
	return func

foo = test(foo)


