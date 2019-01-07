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


print(Dog.__dict__)  # 类Dog的所有属性（数据属性和方法属性），字典形式
print(Dog.__base__)  # 类Dog类继承的最顶层的类，所有类的父类
print(Dog.__bases__) # 类Dog继承的所有类，元祖形式
print(Dog.__class__) # 类Dog的类型
print(Dog.__module__) # 类Dog所属的模块

Dog.shout()  #
Dog.eat('tt') # 类调用带self的方法属性，如果在方法中没有用到实例的特殊属性，参数可以任意写