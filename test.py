#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

principal = 1000
rate = 0.05
year = 1
numberyear = 5
while year <= numberyear:
    principal = principal * (1 + rate)
    print('%3d  %0.2f' % (year,principal))
    year += 1

