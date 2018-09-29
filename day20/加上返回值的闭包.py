#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time


def timer(func):
	def wrapper():
		start_time = time.time()
		# res就是test的返回值
		res = func()
		stop_time = time.time()
		print("运行时间是%s" % (stop_time - start_time))
		return res

	return wrapper


@timer
def test():
	time.sleep(3)
	print("函数运行结束")
	return "这是test的返回值"


print(test())
