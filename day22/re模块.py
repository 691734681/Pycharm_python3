#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 12+(34*6+2-5*(2-1))

import re

"""
re模块的常用方法:findall(),search(),match(),split(),sub(),subn(),finditer()
"""
s = 'alex36wu34lin33yuan35'

# finditer和findall差不多，返回所有匹配到的内容，但是不是以列表的形式，是迭代器.
# res = re.finditer('[a-z]+',s)
# print(res)
# for i in res:
#     print(i.group(),' * ',end = '')

# subn和sub差不多，返回的是替换好的字符串和替换的次数
# res = re.subn('\d+','%',s)
# print(res)

# sub将字符串中匹配的正则用指定字符或字符串替代
# res = re.sub('\d+','%',s)
# print(res)

# finall方法会将所有匹配到的内容以列表的形式返回
# res = re.findall('[a-z]+',s)
# print(res)

# search方法会返回第一个匹配到的内容，并且返回的结果是个对象，查看匹配内容使用返回对象的group方法
# res = re.search('[0-9]+',s)
# print(res)
# print(res.group())

# match方法和search方法类似，也是匹配第一结果，返回一个对象，使用group方法查看返回的具体内容，区别是match方法匹配时，只匹配开头，类似于在正则中添加了^
# res = re.match('[a-z]+',s)
# print(res)
# print(res.group())
# res = re.match('[0-9]+',s)
# print(res)

# split方法是按正则分割字符串，返回一个分割好的列表
# res = re.split('[a-z]',s)
# print(res)



# 匹配（2-1）
# res = re.findall('\([^()]+\)','12+(34*6+2-5*(2-1))')
# print(res)


"""
分组的原则
1. 如果没有括号则返回匹配到的所有内容
2. 如果有一个括号则返回匹配到的内容中括号所包含的内容
3. 有几个括号则返回几个内容
"""
s = 'abc def hij klm nop qrs uvw'
res = re.findall('\w+\s+\w+',s)
print(res)
res = re.findall('(\w+)\s+\w+',s)
print(res)
res = re.findall('((\w+)\s+\w+)',s)
print(res)

# 分组的另一种写法
# s = 'alex36wu34lin33yuan35'
# res = re.search('(?P<name>[a-z]+)(?P<age>\d+)',s)
# print(res)
# print(res.group('name'))
# print(res.group('age'))



