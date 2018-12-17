#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    # 创建一个队列
    simqueue = Queue()
    # 变量列表将名字放入队列
    for name in namelist:
        simqueue.enqueue(name)
    # 当队列大于1时不断循环
    while simqueue.size() > 1:
        for i in range(num):
            # 将队首的元素弹出并放入队尾
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    # 循环结束后只剩一个元素
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))