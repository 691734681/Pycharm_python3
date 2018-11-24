#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time

#  装饰器中闭包函数有返回值和参数

# 装饰器
def timer(func):
	def wrapper(*args,**kwargs):
		start_time = time.time()
		res = func(*args,**kwargs)
		stop_time = time.time()
		print('函数运行时间是 %s' % (stop_time - start_time))
		return res
	return wrapper

# 被装饰函数
@timer
def test(name,age):
	time.sleep(5)
	print('my name is %s age %s' % (name,age))
	return 'test over'

test('alex',18)