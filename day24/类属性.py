#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Chinese:
    """Chinese class"""
    country = 'china'
    local = 'asia'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def play_ball(self):
        print('%s is playing ball' % self.name)

    def work(self):
        print('%s is working now' % self.name)

# 修改类数据属性
Chinese.country = 'japan'
print(Chinese.__dict__)

# 增加类数据属性
Chinese.skin = 'yellow'
print(Chinese.__dict__)

# 删除数据属性
del Chinese.skin
print(Chinese.__dict__)

# 增加方法属性
def eat(self):
    print('eat something')

Chinese.eat = eat
print(Chinese.__dict__)

# 修改方法属性
def play_ball(self):
    """method"""
    print('%s is playing basketball' % self.name)

Chinese.play_ball = play_ball
print(Chinese.__dict__)



