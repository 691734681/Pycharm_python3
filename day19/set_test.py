#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# set(集合):不能有重复元素,集合元素不能是可变元素
# s = {1, 2, 3, 1}
s1 = set("hello")
print(type(s1))
print(s1)

# 遍历集合
for i in s1:
	print(i)

s1.update("ops", "test", (100, 1000))
print(s1)

s2 = set("alex")
s3 = set("alexexex")
print(id(s2))
print(id(s3))
print(s2 == s3)
print(s2 is s3)
print(set("alex") == set("alexex"))