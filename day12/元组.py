#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

tu = (111,22,33,444)
# 元组的常用操作
# 元组不能修改指的是元组的一级元素不能修改，但是内部的二级非元组元素可以修改

# 索引，切片
print(tu[0])
print(tu[0:3])

# for循环
for item in tu:
	print(item,end = ' ')
print()

# 元组不能修改指的是元组的一级元素不能修改，但是内部的二级非元组元素可以修改
tu2 = (111,'alex',(11,22),[(33,44)],True,44)
tu2[3][0] = 567
print(tu2)

# 统计元素出现次数
print(tu2.count(111))

# 返回指定元素在元组的索引
print(tu.index('alex'))









