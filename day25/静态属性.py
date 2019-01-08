#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Room:
    """Room"""
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    """
    加property的作用：该方法就变成一个属性，实例调用可以像调用属性一样调用这样的方法
    """
    @property
    def cal_area(self):
        """cal_area"""
        return self.width * self.length

    def cal_volume(self):
        """cal_volume"""
        return self.height * self.length * self.height

r = Room(10,10,10)
print(r.__dict__)
print(r.cal_area)  # 调用该方法时没有括号
print(r.cal_volume())  # 调用该方法时加括号



