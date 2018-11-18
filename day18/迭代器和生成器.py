#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 三元表达式
name = 'alex'
res = 'sb' if name == 'alex' else 'shuai'
print(res)

# 列表解析 ：生成列表的一种方法
l = [ i for i in range(5)]
print(l)
l2 = [i for i in range(10) if i % 2 == 0]
print(l2)

# 迭代器 ：必须要有__next__()方法
"""
序列中的 字符串，列表，元组，字典，集合，虽然是可迭代对象，但是不是迭代器
他们使用for循环迭代时，是for调用了他们类中的__iter__()方法，将他们变成迭代器
"""
l = [1,2,3,4,5]
iterator_l = l.__iter__()
"""
print(iterator_l.__next__())
print(iterator_l.__next__())
print(iterator_l.__next__())
print(iterator_l.__next__())
print(iterator_l.__next__())
print(iterator_l.__next__()) # 列表中只有5个元素，当迭代到第六个元素时，会报错 StopIteration
"""

# 使用while遍历
while True:
	try:
		print(iterator_l.__next__())
	except StopIteration:
		print('迭代结束')
		break


# 生成器: 自动生成可迭代对象，即生成器有__next__()方法
# 生成器的两种表现形式 1.生成器函数 2.生成器表达式

# 生成器函数:将函数中return替换成yield即可，一个函数可以有多个yield
def test():
	l = [i for i in range(10)]
	yield l

r = test()
print(r)

for i in r:
	print(i,end = ' ')
print()


# 生成器表达式：将列表解析的中括号改成小括号即可
r2 = (i for i in range(10))
print(r2)
for i in r2:
	print(i,end = ' ')
