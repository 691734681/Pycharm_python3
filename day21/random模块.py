#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random

# 0到1间的随机数
res = random.random()
print(res)

# 指定范围内的随机整数
res = random.randint(1,10)
print(res)

# 指定范围内的随机数（小数）
res = random.uniform(1,10)
print(res)


# 从指定序列中随机返回一个元素
l = [1,'a',2,'b']
res = random.choice(l)
print(res)

# 从指定序列中返回指定个数的元素
res = random.sample(l,2)
print(type(res))
print(res)

# 随机改变序列顺序
random.shuffle(l)
print(l)


# 练习随机生成一个字母加数字的4位验证码
def v_code():
	code = ''
	for i in range(5):
		num = str(random.randint(0,9))
		l_a = chr(random.randint(65,90))
		s_a = chr(random.randint(97,122))
		code = code + random.choice([num,l_a,s_a])
	return code

code = v_code()
print(code)

