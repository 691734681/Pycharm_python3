#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
filter函数的使用:
格式:filter(func,list_num)
func:是一个函数，如果函数结构简单可以用lambda
list_num:是一个可迭代序列
作用：是通过func函数处理可迭代序列中的每个值，会过滤掉为false的值
返回：返回的是一个可迭代序列
"""

movie_people = ['sb_alex','sb_wupeiqi','linhaifeng','sb_yuanhao']

# 将列表中带有sb的过滤
def filter_sb(name):
	return not name.startswith('sb')

res = filter(filter_sb,movie_people)
print(list(res))