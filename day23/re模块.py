#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# re模块
import re

# 将匹配到的结果，以列表形式返回
res = re.findall("[a-z]{3}", "abc2432adg32abc")
print(res)

# 只配第一个结果，返回的是对象
res = re.search("[a-z]{3}", "abc2432adg32abc")
print(res)
print(res.group())

# match重头开始匹配，只匹配第一个结果，返回的是对象
res = re.match("\d+", "alex36wusir34xialv33")
print(res)
res = re.match("\d+", "56alex36wusir34xialv33")
print(res)
print(res.group())

# 按照指定内容分割，返回的是列表
res = re.split("[ |]", "hello abc|def")
print(res)

# 替换，可以指定或不指定替换次数
s = "a1b2c3d4e5f6g"
res = re.sub("\d+","A",s)
print(res)
res = re.sub("\d+","A",s,2)
print(res)

# 将要匹配的正则编译
com = re.compile("\d")
res = com.findall("abc2dag4")
print(res)

