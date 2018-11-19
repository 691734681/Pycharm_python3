#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 集合分为可变集合(set)和不可变集合(frozenset) : 集合中元素不可重复
# 集合的创建方式
"""
# 方式一:直接创建
s = {1,2,3,4,5,6,1,2,3,4,5,6}
print(type(s))
print(s)
# 方式二; set() 参数可以是字符串，列表(列表中的值必须是不可变的)，元组，集合，字典
s2 = set('alex li')
print(s2)
"""

li = [2,3,'alex']
s = set(li)
print(s)

# 添加方法add():参数作为整体加入集合
# s.add('uu')
# print(s)

# 更新方法update:将参数作为序列遍历加入集合
# s.update('ops')
# print(s)

# 删除remove
# s.remove(2)
# print(s)

# 随机删除
s.pop()
print(s)

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])
# 交集
print(a.intersection(b))

# 合集
print(a.union(b))

# 差集
print(a.difference(b))

# 反向差集
print(a.symmetric_difference(b))
