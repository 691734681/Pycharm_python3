#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

class Indexer:
    def __getitem__(self, index):
        return index ** 2

I = Indexer()
l = [I[i] for i in range(5)]
print(l)
