#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

s1 = '1 + 2 * ( 4 + ( 2 + 2 ) + ( 1 + 2 ))'
s2 = re.sub('\s+','',s1)
print(s2)
# s3 = re.search('\([^()]+\)',s2)
# print(s3)

def qu_kuo_hao(s):
    """qu_kuo_hao"""
    while True:
        res = re.search('\([^()]+\)',s)
        if not res:
            break
        print(res)

    return res

qu_kuo_hao(s2)







