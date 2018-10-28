#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 使用while循环输出1,2,3,4,5,6,8,9,10
for n in range(11):
	if n != 7:
		print(n)

# 求1-100的所有数和
"""
s1 = 0
for n in range(101):
	s1 += n
print(s1)
"""

# 输入1-100内奇数
"""
for n in range(100):
	if n % 2 != 0:
		print(n)
"""

# 输出1-100内偶数
"""
for n in range(100):
	if n % 2 == 0:
		print(n)
"""

# 求1+2+3+...+99的和
"""
s2 = 0
for n in range(100):
	s2 += n
print(s2)
"""

# 用户登录（三次机会）
"""
count = 0
while count < 3:
	name = input("please enter your name: ")
	if name == 'admin':
		print("login success")
		break
	count += 1
else:
	print('times out')
"""