#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 字典
# key只能是不可变的元素，（列表，字典不能作为key）
info = {
	"k1": 18,
	"k2": True,
	"k3": [
		11,
		22,
		33,
		{
			"kk1": "vv1",
			"kk2": "vv2",
			"kk3": (11, 22)
		}
	],
	"k4": (11, 22, 33, 44),
	True: 123
}
# print(info)
#
# # 通过key取值
# print(info["k1"])
# print(info["k3"][3]["kk3"][0])
#
# # 删除键值对
# del info[True]
# print(info)
#
# # 循环key
# for key in info:
# 	print(key)
#
# for key in info.keys():
# 	print(key)
#
# # 循环value
# for key in info:
# 	print(info[key])
#
# for value in info.values():
# 	print(value)

# 循环key和value
for item in info.items():
	print(item)

for key, value in info.items():
	print(key, "==", value)
