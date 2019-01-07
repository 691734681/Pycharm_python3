#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

country = 'usa'

class Chinese:
    """Chinese"""
    country = 'china'

    def __init__(self,name):
        self.name = name
        print(country)  # 不是通过 .属性调用的变量，其查找的属性不是类中的或方法中的是全局变量
        print(self.country)
        print(Chinese.country)

    def work(self):
        """work"""
        print('% is working now' % self.name)

p1 = Chinese('wangcai')

p1.country = 'japan' # p1 修改的数据属性只是其自身的，不会影响到类中的数据属性；方法属性也一样 , 但是一般不会修改对象的方法属性
print(p1.country)
print(Chinese.country)





