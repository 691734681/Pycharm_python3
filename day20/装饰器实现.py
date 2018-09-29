#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-
import time


# 装饰器的框架
def timer(func):
	def wrapper():
		start_time = time.time()
		# print(func)
		func()
		stop_time = time.time()
		print("函数话费的时间是：%s" % (stop_time - start_time))

	return wrapper

@timer
def test():
	time.sleep(3)
	print("test函数运行完毕")


# print(test)
# @timer：就相当于做了test = timer(test)
#test = timer(test)
test()



