#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

tu = (111, 22, 33, 55)
# 元组的元素不可修改，元组不能增加或删除

# 索引取值
v = tu[0]
print(v)

# 切片
v = tu[0:2]
print(v)

# 循环
for i in tu:
	print(i)

# 字符串转元组
s = "1234"
tu = tuple(s)
print(tu)

# 如果元组内部有列表，其中的列表可以被修改
tu = (111, "alex", (11, 22), [(33, 44)], True, 33, 44)
tu[3][0] = "hello"
print(tu[3])
