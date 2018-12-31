#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import shelve

"""
shelve和json,pickle一样都是做数据序列化存取的 
shelve存取和json，pickle不一样
"""

# 存数据
# f = shelve.open('test_shelve.txt') # 获取的 f 就相当于创建了一个字典，这里的文件名不能是已经存在的
# f['stu1'] = {'name':'alex','age':18}
# f['stu2'] = {'name':'linhaifeng','age':20}
# f.close()

# 读取数据
f = shelve.open('test_shelve.txt')
print(f.get('stu1').get('name'))
f.close()