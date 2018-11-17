#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
文件处理流程：
1.打开文件，得到文件句柄并赋值给一个变量
2.通过句柄对文件进行操作
3.关闭文件
"""

# 因为我的电脑使用的是中午，即默认gbk编码，所以要open这里要指定encoding=utf8
# 注：open默认的是系统的编码格式
# f = open('陈粒.txt',encoding = 'utf-8')
# data = f.read()
# print(data)
# f.close()

"""
文件操作模式
1.只读: r(默认文件打开模式) , r+(读写)
2.只写: w , w+(写读)
3.追加: a , a+(写读)
"""
f = open('xxx',encoding = 'utf-8')

# 文件是否可读readable()
#print(f.readable())

# 读取全部
data = f.read()
print(data)

# 读一行readline()，然后指针到下一行
# 加strip()目的是消除多余空行，或者使用end=''
# print(f.readline(),end = '')
# print(f.readline(),end = '')

# readlines()读取所有行，放入一列表中
# data = f.readlines()
# print(data)

#关闭文件
f.close()

