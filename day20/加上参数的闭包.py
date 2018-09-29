#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time


def timer(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		# res就是test的返回值
		res = func(*args, **kwargs)
		stop_time = time.time()
		print("运行时间是%s" % (stop_time - start_time))
		return res

	return wrapper


@timer
def test(name, age):
	time.sleep(3)
	print("%s,%s" % (name, age))
	print("函数运行结束")
	return "这是test的返回值"


print(test("alex", 18))

print("=" * 50)


@timer
def test2(name, age, gender):
	time.sleep(3)
	print("%s,%s,%s" % (name, age, gender))
	print("函数运行结束")
	return "这是test2的返回值"


print(test2("alex", 19, "男"))
print("="*50)
print(test2("alex",19,gender="男"))
