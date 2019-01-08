#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

s1 = '1 + 2 * ( 4 + ( 2 + 2 ) + ( 1 + 2 ))'
s2 = re.sub('\s+','',s1)
print(s2)
# s3 = re.search('\([^()]+\)',s2)
# print(s3)

# def qu_kuo_hao(s):
#     """qu_kuo_hao"""
#     while True:
#         res = re.search('\([^()]+\)',s)
#         if not res:
#             break
#         res = res.group()
#         temp = res
#         # print(res)
#         while not res[1:-1].isdigit():
#             temp2 = re.search('(\d+)([+\-]+)(\d+)',res)
#             num1 = temp2.group(1)
#             oper = temp2.group(2)
#             num2 = temp2.group(3)
#
#     return res
#
# qu_kuo_hao(s2)

def cal(s):
    """cal"""
    while not s.isdigit():





