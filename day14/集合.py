#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 集合由不同元素组成(元素不能重复)，无序，只能存放不可变类型
# 定义集合的两种方法set()函数(参数是可迭代类型)，直接使用大括号{}
#s1 = set('hello')
#s = {'hello','world','alex','wupeiqi',}

s = {1,2,3,4,5,6}

# 集合的常用方法

# 添加
s.add('3')
s.add(None)
print(s)

# 清空
"""
s.clear()
print(s)
"""

# 拷贝
s1 = s.copy()
print(s1)

# 删除(随机删除一个，并返回删除值)
v = s.pop()
print(s, ' ',v)

# 删除(删除指定元素)
s.remove(3)
print(s)

# 删除
s.discard('sb') # 如果元素不存在不会报错
print(s)

# 更新
s.update({'a','b'})
print(s)

