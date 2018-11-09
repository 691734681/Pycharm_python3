#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

#
def test(x):
	y = 2 * x + 1
	return y

# 打印函数地址
print(test)
# 打印函数执行后的返回结果
print(test(4))

# 函数的参数
def test(x,y,z):
	print(x,y,z,end = ' ')
	print()

# 按照位置参数调用，参数一一对应
test(1,2,3)
# 按照关键字参数调用，参数位置可以不一一对应
test(z = 4,y = 5,x = 6)
# 位置参数和关键字参数混合调用时，关键字参数必须在最后 （位置参数必须在关键字参数左边）
test(7,8,z = 9)

# 默认参数(y就是默认参数，如果没有传给y实参，y就使用默认值)
def test2(x,y = 'mysql'):
	print(x,y,end = ' ')
	print()

test2('hello')
test2('hello','Oracle')

# 可变长参数
def test3(n,*args,**kwargs):
	print(n)
	print(args)
	print(kwargs)

test3('testtesttest')  # 后面的可变长参数可以不传，就相当于传了一个空元组和一个空字典
test3(1,2,3,4,5,x = 6,y = 7,z = 8)
test3(1,(2,3,4,5,),x = 6,y = 7,z = 8)

