#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

def func():
    print('ok')
    x = 10
    print(x)
    x = yield 1
    print(x)
    yield x

f = func()
r = next(f)
print(r)

r2 = f.send('eee')
print(r2)