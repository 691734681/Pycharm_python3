#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time

# 结构化时间
t = time.localtime() # 本地时间 默认的时间就是时间戳
print(t)

t = time.gmtime() # 格林威治时间 默认的时间就是时间戳
print(t)

# 时间戳
t = time.time()
print(t)

# 字符串时间 系统定义的格式
t = time.asctime() # 传入的参数应该是格式化时间，默认的参数是time.localtime()
print(t)

t = time.ctime() # 传入的参数是时间戳，默认的参数是time.time()
print(t)

"""
结构化时间转换成字符串时间使用 asctime()
时间戳转换成字符串使用 ctime()

时间戳转换成结构化字符串使用 gmtime(),localtime(),传入的参数就是时间戳

结构化时间和自定义的字符串时间相互转换:
	结构化时间转字符串时间使用 strftime() 两个参数 第一个是字符串的格式(自定义)，第二个是格式化时间
	字符串时间转结构化时间使用 strptime() 两个参数 第一个是字符串的格式(自定义)，第二个是格式化时间
"""

# 结构化时间转自定义字符串时间
t = time.localtime()
t = time.strftime("%Y__%m__%d  %H::%M::%S",t)
print(t)
t = time.gmtime()
t = time.strftime("%Y__%m__%d  %X",t) # %X 表示时分秒统一格式
print(t)

# 自定义字符串时间转换成结构化时间
t = '2008--10--08 13:11:11'
t = time.strptime(t,"%Y--%m--%d %H:%M:%S")
print(t)