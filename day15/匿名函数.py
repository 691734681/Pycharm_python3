#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 使用lambda定义匿名函数
func = lambda x,y : x + y
print(func(10,29))

name = 'alex'
func = lambda x : x + '_sb'
print(func(name))


# 匿名函数返回多个值
func = lambda x,y,z: (x,y,z)


