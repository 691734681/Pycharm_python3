#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from abc import ABCMeta,abstractmethod

"""
metaclass = abc.ABCmeta表示该类是个接口，其中的抽象方法由子类去实现，抽象方法需要装饰器 @abstractmethod
"""
class All_file(metaclass = ABCMeta):
    """all_file"""

    @abstractmethod
    def write(self):
        """write"""
        pass

    @abstractmethod
    def read(self):
        """read"""
        pass

class Dish(All_file):
    """Disk"""
    pass

class Memory(All_file):
    """memory"""
    def write(self):
        """write"""
        print('memory write')
    def read(self):
        """read"""
        print('memory read')


"""
子类没有实现父类中的抽象方法，直接实例化或调用会报错
d = Dish()
d.write()
"""

m = Memory()
m.read()


