#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Dog:
    """创建一个类，显示其的一些属性"""
    type = 'Dog'

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def shout():
        """shout"""
        print('dog is shouting')

    def eat(self):
        """eat"""
        print('dog eat bone')

dog1 = Dog('waicai',8,'male')
dog2 = Dog('xiaohei',9,'female')


print(dog1.__dict__) # 实例对象没有方法属性，只有数据属性
dog1.eat() # 实例dog1调用方法时，是从类的方法属性中查找

"""
dog1.shout会报错，因为实例在调用方法时，会将自己传入进去，导致报错
TypeError: shout() takes 0 positional arguments but 1 was given
"""
# dog1.shout()

