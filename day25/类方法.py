#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Room:
    """Room"""
    type = 'class'
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    # 加classmethod的作用：该方法就变成一类方法即绑定到类，调用时自动将自身做为参数传入
    @classmethod
    def cal_area(cls):
        """cal_area"""
        return cls.type

    # 有参数self的方法自动绑定到对象，调用时将调用的实例对象做为参数传入
    def cal_volume(self):
        """cal_volume"""
        return self.height * self.length * self.height

print(Room.__dict__)
print(Room.cal_area)
print(Room.cal_volume)

r = Room(10,10,10)
print(r.cal_volume)

print(Room.cal_area())



