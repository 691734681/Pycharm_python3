#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
def fib(n):
	fibs = [1,1]
	if n <= 2:
		return fibs
	for i in range(n-2):
		fibs.append(fibs[-2] + fibs[-1])
	return fibs

fibs = fib(10)
print(fibs)
"""

# 递归的一个例子
def cal(n):
	print(n)
	if int(n/2) == 0:
		return n
	return cal(int(n/2))

cal(9)


# 递归实现斐波那契数列
def fibs(n):
	if n < 0:
		return -1
	if n == 1 or n ==2:
		return 1
	return fibs(n-1) + fibs(n-2)

res = fibs(4)
print(res)