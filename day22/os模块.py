#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import time
import os

# 获取当前文件工作目录
# path = os.getcwd()
# print(path)

# 改变当前目录
# os.chdir(r'c:/')
# print(os.getcwd())

# 生成目录（只能建立单层）
# os.mkdir('os_test')

# 生成目录（可建立多层）
# os.makedirs('os_test/test')

# 删除目录（如果删除目录的上层目录没有文件或其他文件夹，则也会被删除）
# os.removedirs('os_test/test')

# 删除目录（如果目录不为空，则不能删除）
# os.rmdir('test')

# 列出指定目录下所有文件和文件夹
# res = os.listdir('./')
# print(res)

# 删除一个文件
# os.remove('test/test.py')

# 重命名一个文件或文件夹
# os.rename('test/t.py','test/test.py')

# 获取文件或目录的信息
# res = os.stat('os模块.py')
# print(res)

# 获取当前操作系统下的路径分隔符
# sep = os.sep
# print(sep)

# 获取当前操作系统的换行符
# sep = os.linesep
# print(sep)

# 获取当前操作系统的文件路径分隔符
# sep = os.pathsep
# print(sep)

# 获取当前系统的平台
# plat = os.name
# print(plat)

# 执行一条cmd或shell命令
# os.system("dir")

# 获取系统环境变量
# res = os.environ
# print(res)

# 获取文件的绝对路径
path = os.path.abspath('os模块.py')
print(path)

# 将指定路径分割成路径和文件名以元组形式返回 (参数是绝对路径)
# t = os.path.split(os.path.abspath('os模块.py'))
# print(t)

# 获取指定文件的路径 (参数是绝对路径)
path = os.path.dirname(os.path.abspath('os模块.py'))
print(path)

# 获取指定路径中文件的名称
file_name = os.path.basename(os.path.abspath('os模块.py'))
print(file_name)

# 判断文件是否存在
# b = os.path.exists('os模块.py')
# print(b)

# 判断路径是否是绝对路径
# b = os.path.isabs(os.path.abspath('os模块.py'))
# print(b)

# 判断路径是否是目录
# b = os.path.isdir(os.path.abspath('os模块.py'))
# print(b)

# 判断路径是否是文件
# b = os.path.isfile(os.path.abspath('os模块.py'))
# print(b)

# 将路径和文件名组合成完整路径
# path,name = os.path.split(os.path.abspath('os模块.py'))
# # print(path,' * ',name)
# # abspath = os.path.join(path,name)
# # print(abspath)

# 获取指定目录或文件的最后访问时间
# t = os.path.getatime('os模块.py')
# print(time.ctime(t))

# 获取指定目录或文件的最后修改时间
t = os.path.getmtime('os模块.py')
print(time.ctime(t))