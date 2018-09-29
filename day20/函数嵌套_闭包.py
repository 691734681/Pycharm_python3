#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 函数嵌套：在一个函数中定义另一个函数
def father(name):
	print("from father %s" % name)

	def son():
		print("from son")

		def grandson():
			print("from grandson")

		grandson()

	son()


father("林海峰")

print("=" * 50)


# 闭包：简单说就是内部函数调用外部函数的变量
def outer():
	m = 1

	def inner():
		n = 2
		return m + n

	return inner


inner = outer()
print(inner())
