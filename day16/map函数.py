#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
map函数的使用:
格式:map(func,list_num)
func:是一个函数，如果函数结构简单可以用lambda
list_num:是一个可迭代序列
作用：是通过func函数处理可迭代序列中的每个值
返回：返回的是一个可迭代序列
"""

# 例如：将下面的列表中的每个值加1
num_l = [1,2,10,5,3,7]

def add_one(x):
	return x + 1

res = map(add_one,num_l)
print(list(res))

# 使用lambda替代add_one
res2 = map(lambda x : x + 1,num_l)
print(list(res2))

# 将下面的字符串改成大写
s = 'linhaifeng'

def s_upper(x):
	return x.upper()

res_s = map(s_upper,s)
print(list(res_s))

# 使用lamdba函数替代s_upper
res_s2 = map(lambda x : x.upper(),s)
print(list(res_s2))
