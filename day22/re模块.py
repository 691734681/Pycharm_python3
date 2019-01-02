#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 12+(34*6+2-5*(2-1))

import re

# 匹配（2-1）
res = re.findall('\([^()]+\)','12+(34*6+2-5*(2-1))')
print(res)


"""
分组的原则
1. 如果没有括号则返回匹配到的所有内容
2. 如果有一个括号则返回匹配到的内容中括号所包含的内容
3. 有几个括号则返回几个内容
"""
# s = 'abc def hij klm nop qrs uvw'
# # res = re.findall('\w+\s+\w+',s)
# # print(res)
# # res = re.findall('(\w+)\s+\w+',s)
# # print(res)
# # res = re.findall('((\w+)\s+\w+)',s)
# # print(res)

# 分组的另一种写法
s = 'alex36wu34lin33yuan35'
res = re.search('(?P<name>([a-z]+))',s)
print(res.group('name'))



