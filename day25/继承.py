#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Father:
    """Father"""
    money = 10
    dad = 'father'

    def __init__(self,name):
        self.name = name

class Son(Father):
    """Son"""
    money = 100


"""
子类继承父类即继承父类的数据属性和方法属性
"""
s = Son('cici') # 子类中没有初始化方法，就调用父类中的初始化方法
print(s.money)  # 子类中有money属性，就调用自己的money属性
print(s.dad)    # 子类中没有dad属性，就调用父类中的dad属性

