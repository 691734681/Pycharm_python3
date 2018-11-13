#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 定义在py文件最外层的变量就是全局变量
# 定义在类或方法中的变量就是局部变量

"""
name = 'lhf'  # 全局变量

def change_name():
	global name # 加一个global，则方法中的name就是全局变量了
	name = '帅了一比'
	print(name)

# 在方法在内部使用global关键字，放在方法内部最上方

change_name()
print(name)
"""

name = '海风'
# 嵌套函数中的变量 : 就近原则，先找同级再找上层
def huangwei():
	name = 'huang'
	print(name)
	def liuyang():
		name = 'liu'
		print(name)
		def nulige():
			#global name
			nonlocal name # 指的是上一层的变量
			print(name)
		nulige()
	liuyang()
	print(name)

huangwei()



