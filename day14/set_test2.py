#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

python_l = ["lcg", "szw", "zjw"]
linux_l = ["lcg", "szw", "sb"]

# 在两个列表中都存在的元素(求交集)
python_linux_l = []
for pname in python_l:
	if pname in linux_l:
		python_linux_l.append(pname)

print(python_linux_l)
# 使用set中方法实现上面的功能
s_p = set(python_l)
s_l = set(linux_l)
v = s_p.intersection(s_l)
print(v)
v = s_l & s_p
print(v)

# 求并集
v = s_p.union(s_l)
print(v)
v = s_l | s_p
print(v)

# 求差集
v = s_p.difference(s_l)
print(v)
v = s_p - s_l
print(v)

# 交叉补集
v = s_p.symmetric_difference(s_l)
print(v)
v = s_p ^ s_l
print(v)

# 是否是子集
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))

# 是否是父集
print(s2.issuperset(s1))

# 更新
s1.update(s2)
print(s1)

# 交集是否为空
s1 = {1, 4}
s2 = {2, 3}
v = s1.isdisjoint(s2)
print(v)
