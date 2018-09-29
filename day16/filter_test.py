#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 内置函数 filter
movie_people = ["alex", "wupeiqi", "yuanhao", "sb_lihaifeng"]

# filter过滤指定元素，返回和map函数一样是一个迭代器
res = filter(lambda n: n.startswith("sb"), movie_people)
print(res)
li = list(res)
print(list(res))
print(li)
