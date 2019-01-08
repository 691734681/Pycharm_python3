#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Room:
    """Room"""

    def __init__(self,length,width,heigth):
        self.length = length
        self.width = width
        self.heigth = heigth

    # 静态方法不绑定类或对象，只是类的工具包
    @staticmethod
    def cal_area():
        """cal_area"""
        return '类的工具包'

print(Room.cal_area())

r = Room(10,10,10)
print(r.cal_area())