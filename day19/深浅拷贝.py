#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import copy
# 深拷贝和浅拷贝
# 浅拷贝：一级元素不会被拷贝影响，二级元素(元素中包含的元素)会被影响
# 深拷贝：所有元素都不会被影响
s = [[1,2],'alex','alvin']
s_copy = s.copy()
s_deepcopy = copy.deepcopy(s)

# 如果修改深拷贝的[1,2]不会影响原列表
s_deepcopy[0][0] = 10
print(s_deepcopy)
print(s)

# 如果修改浅拷贝的[1,2]会影响到原列表
s_copy[0][0] = 100
print(s_copy)
print(s)


