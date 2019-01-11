#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Super:
    """super"""
    def method(self):
        """method"""
        print('in super.method')
    def delegate(self):
        """delegate"""
        self.action()

class Inheritor(Super):
    """inheritor"""
    pass

class Replacer(Super):
    """replacer"""
    def method(self):
        """method"""
        print('in replace.method')

class Extender(Super):
    """extender"""
    def method(self):
        """method"""
        print('starting extender.method')
        super.method()
        print('ending extender.method')

class Provider(Super):
    """provider"""
    def action(self):
        """action"""
        print('in provider.action')

if __name__ == __main__:
    for klass in (Inheritor,Replacer,Extender):
        print(klass.__name__,' ***** ',klass().method())
    print('Provider...')
    print(Provider().delegate())

