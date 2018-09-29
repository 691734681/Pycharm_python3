#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

# 用正则表达式解决一个算式
s = "1-2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14)) - (-4*3)/ (16-3*2) )"
# print(eval(s))

# 去掉空格
s = re.sub("\s", "", s)
# print(s)


