#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

dic = {'alex':300,'wupeiqi':100,'yuanhao':200}
res = zip(dic.values(),dic.keys())
l = list(res)
print(l)
sorted(l,key = lambda t : t[0])
print(l)
