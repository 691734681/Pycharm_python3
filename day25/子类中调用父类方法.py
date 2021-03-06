#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Fu:
    """fu"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def drink_water(self):
        """drink_water"""
        print('%s drink water' % self.name)

class Zi(Fu):
    """Zi"""
    def __init__(self,name,age,school):
        # 下面两句话都可以实现子类中调用父类方法，super较常用
        # Fu.__init__(self,name,age)
        super().__init__(name,age)
        self.school = school

    def drink(self):
        """drink"""
        # Fu.drink_water(self)
        super().drink_water()
        print('drink_orange')

z = Zi('wai',18,'xiaoxue')
z.drink()
