#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

li = [1, 12, 9, "age", ["石正文", ["19", 10], "庞麦郎"], "alex", True]

# 列表常用方法演示

# 追加
li.append(5)
li.append([1234, 2323])
print(li)

# 清空
li.clear()
print(li)

# 拷贝
li = [1, 12, 9, "age", ["石正文", ["19", 10], "庞麦郎"], "alex", True]
v = li.copy()  # 浅拷贝
print(v)

# 计算元素的个数
v = li.count(1)
print(v)

# 扩展
li.extend(["9899", "budeliao"])
print(li)

# 找索引位置 (只找第一个)
v = li.index(12)
print(v)

# 在指定位置插入值
li.insert(0, "test")
print(li)

# 删除一个值，并返回 （默认删最后一个）
v = li.pop()
print(v)
v = li.pop(0)
print(v)
print(li)

# 删除指定值
li.remove(12)
print(li)

# 反转
li.reverse()
print(li)

# 排序
li = [1, 5, 2, 8, 9]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

