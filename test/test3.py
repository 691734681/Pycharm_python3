#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import string

s = string.ascii_letters
n = string.digits
l = list(s)
l.extend(list(n))
print(l)