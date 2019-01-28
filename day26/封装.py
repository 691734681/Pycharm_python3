#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 如何访问python类中的私有变量

class People:
	"""people"""
	'''
	变量或方法前以一个或2个下划线开头的都是私有的。
	但是以一个下划线开头的私有属性只是约定，实际上还是可以直接访问的
	以两个下划线开头的私有属性，不能直接访问，可以通过方法或其在类属性的被修改的名字访问
	'''
	_age = 18
	__gender = 'female'

	def __init__(self):
		pass

	def get_gender(self):
		"""get_gender"""
		return self.__gender

p = People()
print(People.__dict__)
# 以一个下划线开头的私有属性，无论是类还是实例都可以直接访问，但是不要这么做
print(People._age)
print(p._age)

# 以两个下划线的私有属性，通过其在类属性中的新名字或方法访问
print(People._People__gender)
print(p._People__gender)
print(p.get_gender())

# 所有在python中并没有像Java中那样真正的封装私有属性