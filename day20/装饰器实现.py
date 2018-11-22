#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time

# 装饰器完成计算test的运行时间 timer()就是一个装饰器
def timer(func):
	def wrapper():
		start_time = time.time()
		#print(func)
		func()
		stop_time = time.time()
		print('运行时间是%s' % (stop_time - start_time))
	return wrapper

@timer   # @timer 就相当于test = timer(test)  装饰器要修哪个函数就把 @装饰器名（@timer）放在被修饰函数上
def test():
	time.sleep(10)
	print('test函数运行结束')

# test = timer(test)
# test()
