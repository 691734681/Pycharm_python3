#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Super:
    def method(self):
        print('in super.method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in replace.method')

class Extender(Super):
    def method(self):
        print('starting extender.method')
        super.method()
        print('ending extender.method')

class Provider(Super):
    def action(self):
        print('in provider.action')

if __name__ == __main__:
    for klass in (Inheritor,Replacer,Extender):
        print(klass.__name__,' ***** ',klass().method())
    print('Provider...')
    print(Provider().delegate())

