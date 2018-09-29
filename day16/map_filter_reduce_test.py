#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from functools import reduce

# map(func, *iterator)
# 处理序列中的每个元素，得到的结果是一个列表
p = [
	{"name": "alex", "age": 1000},
	{"name": "wupei", "age": 10000},
	{"name": "yuanhao", "age": 9000},
	{"name": "linhaifeng", "age": 18},
]
res = map(lambda x: x.get("age") <= 18, p)
print(res)
print(list(res))
print(list(res))

print("=" * 50)
# filter(func or None, iterator )
# 遍历序列中的元素，判断每个元素，如果是true则留下
p1 = [
	{"name": "alex", "age": 1000},
	{"name": "wupei", "age": 10000},
	{"name": "yuanhao", "age": 9000},
	{"name": "linhaifeng", "age": 18},
]
# 过滤掉age大于18的
res1 = filter(lambda x: x.get("age") <= 18, p1)
print(res1)
print(list(res1))
print(list(res1))

print("=" * 50)
# reduce(func, sequence, init=None)
# 处理一个序列，然后把序列进行合并操作

res2 = reduce(lambda x, y: x + y, range(101))
print(res2)

