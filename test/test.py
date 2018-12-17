#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import string
import random
import time

# l = []
# for i in range(97,123):
#     l.append(chr(i))

l = [chr(i) for i in range(97,123)]

l.append(' ')

print(l)

goal = 'methinks it is a weasel'
# goal = 'abc'

start_time = time.time()

while True:
    t_list = []
    for i in range(len(goal)):
        t_list.append(random.choice(l))
    t_string = ''.join(t_list)
    if t_string == goal:
        print(t_string)
        break
    print(t_string)
    continue

stop_time = time.time()

t = stop_time - start_time
print(t)





