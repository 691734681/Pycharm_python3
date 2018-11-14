#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 函数式编程是一种风格，规范
# 函数中不用变量保存状态,不修改变量,把函数当做参数传递,返回值中包含函数

# 例如:在函数中没有定义变量
"""
n = 1
def increase(n):
	return n + 1


# 把函数当做参数传递
def foo(n):
	print(n)

def bar(name):
	print('my name is %s ' % name)

foo(bar)
foo(bar('alex'))

# 返回值中包含函数
def bar1():
	print('from bar1')

def foo1():
	print('from foo1')
	return bar1

n = foo1()
n()

def handle():
	print('from handle')
	return handle

h = handle()
h()
"""

# 高阶函数：满足两个条件之一：1.接收的参数是函数 2.返回值是函数

# 尾调用：在函数的最后一步调用另外一个函数
# 尾递归：在函数的最后一步递归
def bar(n):
	return n

def foo(x):
	return bar(x) # 在foo函数最后一步调用bar


