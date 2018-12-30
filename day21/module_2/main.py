#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
直接执行这个文件会报错，找不到module_1这个模块
因为python找路径是从上层文件夹开始找
如果要想from module_1 import cal_1在这个文件生效
需要将该包添加到sys.path路径。例如：sys.path.append(路径名)
"""
import sys
import pprint
# 这里的引入是给上层文件夹中bin使用的
from module_1 import cal_1

pprint.pprint(sys.path)
cal_1.add(1,2)

