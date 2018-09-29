#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time

# 时间戳 ：主要用于计算
print(time.time())

# 显示的是结构化时间
# 显示本地时间
t = time.localtime()
print(t)
# 显示格林尼治时间
t2 = time.gmtime()
print(t2)
# 通过该结构化的对象的属性获取想要的时间
print(t.tm_year)

# 字符串时间
print(time.asctime())
print(time.ctime())

# 时间戳，结构化时间，字符串时间的相互转化
# 1.时间戳转化为结构化时间
print(time.localtime(time.time()))
# 2.结构化时间转化为时间戳
print(time.mktime(time.localtime()))
# 3.结构化时间转化为字符串时间
print(time.strftime("%Y-%m-%d",time.localtime()))
print(time.strftime("%Y-%m-%d %X",time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 4.字符串时间转化为结构化时间
print(time.strptime("2016-12-2 11:11:11","%Y-%m-%d %X"))
print(time.strptime("2016-12-2 11:11:11","%Y-%m-%d %H:%M:%S"))

# 等待5秒
time.sleep(5)

import datetime
# datetime常用方法
print(datetime.datetime.now())

