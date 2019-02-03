#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import pprint
import tokenize

reader = open('bonus.py').__next__
print(type(reader),' * ',reader)
tokens = tokenize.generate_tokens(reader)
print(type(tokens),' * ',tokens)
print('*****************')
l = [tokens.__next__() for i in range(10)]
pprint.pprint(l)





