#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random

"""
# 随机数模块常用方法

# 产生0到1的浮点数
print(random.random())
# 产生1到3范围内的整数包括3
print(random.randint(1, 3))
# 产生1到3范围内的整数不包括3
print(random.randrange(1, 3))
# 在指定列表中随机返回一个值
print(random.choice([11, 22, 33]))
# 在指定列表中随机返回，指定个数的值
print(random.sample([11, 22, 33, 44, 55], 2))
# 反复指定范围内的随机浮点数
print(random.uniform(1, 9))

# 将指定的列表，随机排列其中的元素
items = [1, 3, 5, 7, 9]
print(random.shuffle(items))
print(items)
"""
# 生成一个0-9的列表
l = list(range(0, 10))
print(l)
# 生成一个A到Z的列表
l2 = []
for i in range(65, 91):
	l2.append(chr(i))
print(l2)
# 生成一个a到z的列表
l3 = []
for i in range(97, 123):
	l3.append(chr(i))
print(l3)

# 将上面上列表合并
for i in l2:
	l.append(i)
for i in l3:
	l.append(i)

print(l)


# 生成一个验证码函数（数字字母混合）方法1
def v_code(item):
	return random.sample(l, 5)


res = v_code(l)
print(type(res))
print(res)


# 生成一个验证码函数（数字字母混合）方法2
def v_code2():
	res = []
	for i in range(5):
		num = random.randint(0, 19)
		alp = chr(random.randint(65, 90))
		alp2 = chr(random.randint(97, 122))
		temp = random.choice([num, alp, alp2])
		res.append(temp)
	return res

res2 = v_code2()
print(res2)
