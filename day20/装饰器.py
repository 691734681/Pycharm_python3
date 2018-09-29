#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time


# 装饰器：本质就是函数，修饰其他，为其他函数添加附加功能
# 原则：1.不修改被修饰函数源代码，2.不修改被修饰函数调用方式
# 装饰器的知识储备：装饰器 = 高阶函数 + 函数嵌套 + 闭包

def cal(n):
	"""des"""
	# start_time = time.time()
	res = 0
	for i in n:
		time.sleep(0.1)
		res = res + i
	# end_time = time.time()
	# print("函数运行时间是%s" % (end_time - start_time))
	return res


print(cal(range(101)))

# 统计上面函数的运行时间: time加到函数中统计是种不好的方法
# 正确的是使用装饰器

