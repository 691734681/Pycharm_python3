#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import sys,time

# 获取python解释器的版本
print(sys.version)

# 获取操作系统
print(sys.platform)

# 中断并退出程序
# sys.exit()

# 获取python解释器的环境变量
print(sys.path)

# 获取执行文件时获取的参数
args = sys.argv
print(args)

for i in range(100):
    time.sleep(1)
    sys.stdout.write('#')