#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-
'''
# 集合是无序的，存放不可变元素，元素不可重复

# 定义集合
s = {"hello", "1", "world", 2, "alex"}

# 遍历集合
for i in s:
	print(i)

# 将字符串变set
s = set("hello")
print(s)
'''
# 集合常用方法
s = {1, 2, 3, 4, 5, 6}

# 添加元素
s.add("s")
print(s)

# 清空
# s.clear()
# print(s)

# 拷贝
s1 = s.copy()
print(s1)

# 删除(随机删除)
v = s.pop()
print(v)
print(s)

# 删除(指定删除)(没有则报错)
s.remove(5)
print(s)

# 删除（指定删除）（没有不报错）
s.discard(100)
print(s)
