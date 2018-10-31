#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 列表中的元素可以是数字，字符串，列表，元组，字典，布尔值等
# 列表“集合”中可以放任何东西
li = [1,12,9,'age',['石正文',['19',10],'庞麦郎'],'alex',True]

# 索引，切片取值
print(li[3])
print(li[3:5]) #切片结果也是列表

# for循环
"""
for i in range(len(li)):
	print(li[i],end= ' ')
"""
for item in li:
	print(item,end = ' ')
print()

# 列表元素可以被修改
li[1] = 120
print(li)

# 删除元素
del li[1]
print(li)

# 取列表元素中的列表的内容
print(li[3][1][0])

# 字符串转列表
s = '123'
l = list(s)
print(l)

li = [11,22,33,44]
# 列表追加元素
li.append(5)
print(li)

# 复制列表，浅拷贝
li2 = li.copy()
print(li2)

# 计算元素出现的次数
print(li.count(22))

# 扩展列表，参数必须是可迭代的
li.extend('hello')
print(li)

# 查找元素位置 , 返回第一个找到元素的位置，可以指定起始位置
print(li.index(11))
print(li.index(33,0,3))

# 插入元素
li.insert(0,99)
print(li)

# 删除元素
li.pop(0)
print(li)
li.remove(11)
print(li)

li = [11,22,33,22,44]
# 列表反转
li.reverse()
print(li)

# 排序
li.sort()
print(li)


