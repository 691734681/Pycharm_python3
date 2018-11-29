#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

globals = {
    'x':7,
    'y':10,
    'birds':['Parrot','Swallow','Albatross']
}
locals = {}

a = eval('3 * x + 4 * y',globals,locals)
print(a)
print(globals)
#print(locals)