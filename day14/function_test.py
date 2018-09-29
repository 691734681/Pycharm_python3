#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 函数的定义（带参函数）
def test(x):
	"the function description"
	x += 1
	return x


# 打印函数的内存地址
print(test)
# 打印调用函数结果
y = test(1)
print(y)


# 过程的定义（过程就是没有返回值的函数）
def test1():
	print("hello world")


# 位置参数，关键字参数，混合使用参数
def test(x, y, z):
	print(x)
	print(y)
	print(z)


test(1, 2, 3)  # 位置参数：参数的位置一一对应
test(y=1, x=3, z=0)  # 关键字参数：参数通过参数名指定
test(1, 3, z=4)  # 混合使用时位置参数必须在关键字参数左边


# 默认参数
def test(x, type=None):
	print(x)
	print(type)


test(2)  # 如果没有给参数就是使用默认值
test(2, 'type')  # 如果给了参数，就使用所给参数


# 可变参数: *表示元组 ,**表示字典
def test(x, *args, **kwargs):
	print(x)
	print(args)
	print(kwargs)


test(1)
test(1, 2, 3, 4, 5, 6, 7)
test(1, 2, 3, 4, 5, name="test")
test(x=1, arg1=[3, 5], arg2={"name": "test", "age": 18})  # 使用关键参数处理，则后边对应的都变成字典
