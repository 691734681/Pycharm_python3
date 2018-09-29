#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 字典常用方法
dic = {"k1": "v1", "k2": "v2"}

'''
# 创建字典，第一个参数是序列成为字典的值，第二个参数成为值
v = dict.fromkeys(["k1", 123, "999"], 2)
print(v)
v = dict.fromkeys("abc", 1)
print(v)


#获取指定键的值，如果该键没有值，可以指定默认值（默认的是None）
v=dic.get("k4")
print(v)
v = dic.get("k1", -1)
print(v)


# 获取所有键
v = dic.keys()
print(v)


# 获取所有值
v = dic.values()
print(v)


# 获取键值对
v = dic.items()
print(v)


# 删除指定键 ，可以指定返回的默认值
v = dic.pop("k3", -1)
print(v)
print(dic)


# 随机删除键的值
v = dic.popitem()
print(v)
print(dic)


# 给指定键设置值，如果该键有值，则使用原有值
dic.setdefault("k1", 100)
print(dic)
dic.setdefault("k3", "v3")
print(dic)
'''

# 更新键值对
dic.update({"k1": "v11", "k3": "v3"})
print(dic)
dic.update(k1=123, k4="v4")
print(dic)
