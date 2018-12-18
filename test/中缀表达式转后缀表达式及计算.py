#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# s字符串是中缀表达式
s = '1 + 2 * 3 + ( 4 * 5 + 6 ) * 7'
# 对应的后缀表达式是 '1 2 3 * + 4 5 * 6 + 7 * +'
print(eval(s))

"""
中缀表达式转换为后缀表达式的原则
1. 遇到操作数，直接输出
2. 遇到操作符及左括号，将其放入栈中
3. 遇到右括号则将栈中元素开始弹出并输出，直到遇到左括号，括号不输出
4. 遇到操作符，如果比栈顶的操作符优先级低，则开始将栈中元素弹出，直到遇到，优先级更低的操作符或栈弹空，然后再将该操作符放入栈中
"""

# 将s字符串转化为后缀表达式
# 第一步将字符串转为列表
l = s.split(' ')
print(l)
# 遍历列表，按照中缀表达式转后缀表达式的原则进行转换
temp = []
res = []
oper = ['+','-','*','/','(',')']
for i in l:
    if i not in oper:
        res.append(i)
        continue
    if i in oper:
        if len(temp) != 0:
            if i == ')':
                while True:
                    t = temp.pop()
                    if t == '(' or len(temp) == 0:
                        break
                    res.append(t)
            elif i in ['*','/','(']:
                temp.append(i)
            elif i in ['+','-'] and temp[-1] in ['*','/']:
                while True:
                    t = temp[-1]
                    if t != '(':
                        res.append(temp.pop())
                    if len(temp) == 0 or t == '(':
                        temp.append(i)
                        break
        elif len(temp) == 0 and i != ')':
            temp.append(i)

print(temp)
print(res)

while True:
    if len(temp) == 0:
        break
    else:
        res.append(temp.pop())

print(res)
print(' '.join(res))

"""
中缀表达式变前缀表达式的原则变后缀表达式一样，只是遍历列表的时候是从后往前
左右括号的规则相反
"""

