#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 递归演示
ls = []


def test(n):
	"""description"""
	n = int(n / 2)
	ls.append(n)
	print(ls)
	if int(n / 2) == 1:
		return ls
	test(n)


test(10)
print(ls)


# 完成阶乘
# 递归的两种调用方式
# 1.非尾调用 （调用函数本身不在最后一步）
def f(n):
	"""description"""
	if n == 1:
		return 1
	# 最后一行有两步，调用f和n乘f
	return n * f(n - 1)


print(f(4))


# 2.尾调用 （调用函数本身在最后一步）
def f2(n, total):
	"""description"""
	if n == 1:
		return total
	return f2(n - 1, n * total)


print(f2(4, 1))
