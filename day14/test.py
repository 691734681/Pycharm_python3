#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

python_l = ['lcg','szw','zjw']
li_l = ['lcg','szw','sb']

# 打印两个列表相同元素
for i in python_l:
	if i in li_l:
		print(i)

# 使用集合解决上面问题
p_s = set(python_l)
l_s = set(li_l)
print(p_s)
print(l_s)

# 交集
v = p_s.intersection(l_s)
print(v)

# 并集
v = p_s.union(l_s)
print(v)

# 差集
v = p_s.difference(l_s)
print(v)

# 交叉补集
v = p_s.symmetric_difference(l_s)
print(v)

# 判断两个集合是否有交集：无交集返回True
print(p_s.isdisjoint(l_s))

# 判断是否子集关系
print(p_s.issubset(l_s))

