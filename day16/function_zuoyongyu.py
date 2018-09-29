#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 函数作用域
name = "alex"


def foo():
	"""description"""

	# name = "linhaifeng"

	def bar():
		"""description"""
		# name = "wupeiqi"
		print(name)

	# bar()
	return bar


# 将bar函数内存地址给test
test = foo()
print(test)
print(foo())
# 下面两个函数运行结果一样
test()
foo()()
