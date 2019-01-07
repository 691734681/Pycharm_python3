#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

s = '1 + 2 * ( 4 + ( 2 + 2 ) + ( 1 + 2 ))'
s2 = re.sub('\s+','',s)

"""
def kong_Ge(s):
    '''删除多余的空格'''
    res = re.sub('\s+','',s)
    return res

def he_Fa(s):
    '''判断数学表达式是否合法，没有联系操作符，左右括号对称'''
    res = re.findall('[()]',s)
    if not res.count('(') == res.count(')'):
        return '左右括号数量不匹配'
    res = re.search(r'[+\-*/%]{2,}',s2)
    if res:
        return '有多余的操作符'
"""
def kuo_Hao(s):
    """将括号内的数学表达式计算完并替换"""
    while True:
        res = re.search('\([^()]+\)',s)
        if not res:
            break
        temp = res.group()
        res = res.group()[1:-1]
        while not res.isdigit():
            sum = 0


    return s

print(kuo_Hao(s2))



