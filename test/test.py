#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

"""
s = '1 + 2 * ( 4 + ( 2 + 1 + 3 + 2 ) )'
s2 = 1+2*(4+(2+1+3+2))
reg = r'\([^()]+\)'
res = re.search(reg,s)
temp = res.group()
temp = temp[1:-1]
print(temp)
while len(temp) >= 3:
    sum = 0
    if temp[1] == '+':
        sum = int(temp[0]) + int(temp[2])
    temp = str(sum) + temp[3:]
s = re.sub(reg,temp,s)
"""

# """
s = '1213+-123+-21'
# res = re.search('[+\-]+',s)
# print(res.group())
res = re.search('(\d+)([+\-]+)(\d+)',s)
print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(3))
res = s.replace(res.group(0),'Z')
print(res)
# print(res.group(4))
# """