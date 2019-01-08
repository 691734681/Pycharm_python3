#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Z:
    def test(self):
        print('Z')

class A(Z):
    def test(self):
        print('A')

class B(A):
    def test(self):
        print('B')

class C(B):
    def test(self):
        print('A')

class D(Z):
    def test(self):
        print('D')

class E(D):
    def test(self):
        print('E')

class F(E):
    def test(self):
        print('F')

class G(C,F):
    def test(self):
        print('C')

# 继承调用的顺序可以通过__mro__查看

print(G.__mro__)