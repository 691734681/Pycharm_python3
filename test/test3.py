#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Test:
    """Test"""
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        # self.value = self.value + other
        return Test(self.value + other)

    def __mul__(self, other):
        # self.value = self.value * other
        return Test(self.value * other)

t = Test('a')
t += 'b'
print(t.value)
t2 = Test('c')
t2 *= 10
print(t2.value)





