#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 定义在py文件最外层的变量就是全局变量
name = "lhf"


# 定义在子程序中的变量
def test():
	x = 1  # x是局部变量
	print(x)


def change_name():
	name = "帅的很"
	print(name)


change_name()

# 全局变量要大写
NAME = "TEST"


def test1():
	# 全局变量在函数中，如要声明要放在第一行
	global NAME
	print(NAME)


def huang():
	name = "huang"
	print(name)

	def liu():
		name = "liu"
		print(name)

		def hu():
			name = "hu"
			print(name)

		print(name)
		hu()

	liu()
	print(name)


huang()

name = "gangniang"


def weihou():
	name = "chenzhuo"

	def weiweihou():
		nonlocal name  # nonlocal指的是上层变量
		name = "lengjing"

	weiweihou()
	print(name)


print(name)
weihou()
print(name)
