#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class FirstClass:
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data)
    def __add__(self,other):
        return FirstClass(self.data + other)
    def __mul__(self, other):
        self.data = self.data * other

f1 = FirstClass('abc')
f2 = f1 + 'xyz'
f3 = f1 * 3

# print(type(f1),'*****',f1.display())
# print(type(f2),'*****',f2.display())
# print(type(f3),'*****',f3.display())
print(f1)
