#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# os模块
import os

#print(__file__)

# 返回当前文件目录的上级目录
print(os.path.dirname(__file__))

# 返回当前文件的绝对路径
print(os.path.abspath(__file__))

# 返回当前的目录
print(os.getcwd())

# 改变工作目录
os.chdir("test")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

# 新建单个目录
#os.mkdir("test2")
# 新建多层目录
#os.makedirs("a/b/c")

# 删除多层目录（若删除的目录的上层为空，则连上层目录一起删除）
#os.removedirs("a/b/c")
# 删除当个目录
#os.rmdir("test2")

# 列出当前目录所有的文件或目录
print(os.listdir("."))

# 删除文件，不能删目录
#os.remove("test3")

# 重命名文件
#os.rename("test3","test4")

# 返回指定文件的信息(创建时间，大小，修改时间等)
print(os.stat("sss"))

# 当前系统分隔符
print(os.sep)

# 显示当前的操作系统
print(os.name)

# 获取系统变量
print(os.environ)

# 执行一条命令并返回结果
print(os.system("dir"))

# 判断文件是否存在
print(os.path.exists("sss"))

# 判断路径是否是绝对路径
print(os.path.isabs("sss"))

# 判断是否是文件
print(os.path.isfile("sss"))

# 判断是否是文件夹
print(os.path.isdir("sss"))





