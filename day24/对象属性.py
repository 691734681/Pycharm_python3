#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Chinese:
    """Chinese class"""
    country = 'china'

    def __init__(self,name):
        self.name = name

    def play_ball(self):
        """play ball"""
        print('%s is playing ball' % self.name)

p1 = Chinese('wangcai')
print(p1.__dict__)

# 增加数据属性
p1.local = 'asia'
print(p1.__dict__)

# 修改数据属性
p1.name = 'xiaoqiang'
print(p1.__dict__)

# 删除数据属性
del p1.local
print(p1.__dict__)

# 增加方法属性
def work(self):
    """work"""
    print('%s is working now' % self.name)

p1.work = work
print(p1.__dict__)


