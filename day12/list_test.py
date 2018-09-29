#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

li = [1, 12, 9, "age", ["石正文", ["19", 10], "庞麦郎"], "alex", True]

# 索引取值
print(li[3])

# 切片取值
print(li[3:5])

# for循环
for i in li:
	print(i)

# 修改列表元素
li[1] = 120
print(li)

# 删除列表元素
del li[1]
print(li)

# in操作
f = 12 in li
print(f)

# 取出列表中嵌套列表中的19
li = [1, 12, 9, "age", ["石正文", ["19", 10], "庞麦郎"], "alex", True]
print(li[4][1][0])

# 字符串转换为列表
s = "abcdefg"
li = list(s)
print(li)

# 列表转字符串
li = [11, 22, 33, "123", "alex"]
s = ""
for i in li:
	s += str(i)

print(s)


