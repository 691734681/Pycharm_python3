#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# s是后缀表达式的字符串
s = '1 2 3 * + 4 5 * 6 + 7 * +'

"""
后缀表达式的计算原则
1. 遍历表达式，如果遇到的数字则放入栈中
2. 如果遇到的是操作符，则将栈中最顶端的两个数字弹出，结合该操作符预算，并将结果放入栈中
"""

# 计算后缀表达式
# 第一步将后缀表达式字符串转换为列表
l_s = s.split(' ')
print(l_s)
# 创建临时列表做为栈
temp = []
oper = ['+','-','*','/']
# 遍历列表
for i in l_s:
    if i not in oper:
        temp.append(i)
    else:
        t1 = int(temp.pop())
        t2 = int(temp.pop())
        if i == '+':
            temp.append(t1 + t2)
        elif i == '-':
            temp.append(t1 - t2)
        elif i == '*':
            temp.append(t1 * t2)
        elif i == '/':
            temp.append(t1 / t2)

print(temp)

