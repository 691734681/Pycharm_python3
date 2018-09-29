#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import copy

name = [[1, 2], "alex", "alvin"]
# 浅拷贝 : 列表中的子项修改时会影响到原来的数据
name2 = name.copy()
# 修改name2中的"alex"不会影响到name中的"alex"
name2[1] = "linux"
name2[0][0] = 3
print(name)
print(name2)

print("=" * 60)
# 深拷贝: 任何修改都不会影响原来的数据
name3 = copy.deepcopy(name)
name3[1] = "linux"
name3[0][0] = 4
print(name)
print(name3)
