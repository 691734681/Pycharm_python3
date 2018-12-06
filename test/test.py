#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import pprint

f = open('test')
datas = f.readlines()
print(type(datas))
pprint.pprint(datas)
f.close()

print('*' * 60)
print('*' * 60)
print('*' * 60)
print('*' * 60)
print('*' * 60)

l = []

for data in datas:
    if data in l:
        continue
    else:
        l.append(data)

pprint.pprint(l)

f = open('test2.txt','w',encoding = 'utf-8')
for i in l:
    f.write(i)




