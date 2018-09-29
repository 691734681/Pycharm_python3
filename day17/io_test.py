#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 文件处理流程
# 1.打开文件，得到文件句柄并赋值给一个变量
f1 = open("test_utf8", encoding="utf-8")
# f2 = open("test_gbk", encoding="gbk")

# 2.通过句柄对文件进行操作
data1 = f1.read()
print(data1)
print("=" * 50)
# data2 = f2.read()
# print(data2)

# 3.关闭文件
f1.close()
# f2.close()


