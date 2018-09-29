#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 生成器两种表现形式
# 1. 生成器函数 yeild：在函数中用yield取代return，可以有多个yield


def test():
	"""description"""
	yield 1
	yield 2


r = test()
print(r)
print(r.__next__())
print(r.__next__())

# 2. 生成器表达式
eggs = (i for i in range(10))
print(eggs)
print(eggs.__next__())
print(next(eggs))

# 三元表达式
name = "alex"
res = "sb" if name == "alex" else "handsome"
print(res)

# 列表解析
# 通过循环完成一个列表
egg_list = []
for i in range(10):
	egg_list.append("鸡蛋%s" % i)
print(egg_list)
# 使用列表解析完成上面的操作
egg_list2 = ["鸡蛋%s" % i for i in range(10)]
print(egg_list2)
egg_list3 = ["鸡蛋%s" % i for i in range(10) if i > 4]
print(egg_list3)

