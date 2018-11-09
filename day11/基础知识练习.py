#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random


# 执行 Python 脚本的两种方式
"""
python 文件名
文件名
"""

# 简述位、字节的关系
"""
一个字节占8位
"""

# 简述 ascii、unicode、utf-­‐8、gbk 的关系
"""

"""

# 请写出  “李杰”  分别用 utf-8 和 gbk 编码所占的位数
"""
utf-8中一个字符占3个字节，所以占6位
gbk中一个字符占2个字节，所以占4位
"""

# Pyhton 单行注释和多行注释分别用什么？
"""
井号，三个单引号或双引号
"""

# 声明变量注意事项有那些？
"""
字母，数字，下划线；不能以数字开头
"""

# 如有一下变量 n1  =  5，请使用 int 的提供的方法，得到该变量最少可以用多少个二进制位表示？
n1 = 5
print(n1.bit_length())

# 布尔值分别有什么？
"""
True , False
"""

# 阅读代码，请写出执行结果
#     a  =  "alex"
#     b  =  a.capitalize()
#     print(a)
#     print(b)
#     请写出输出结果：
"""
alex
Alex
"""

"""
# 写代码，有如下变量，请按照要求实现每个功能
#     name  =  "  aleX"
name = '   aleX'
#     a.  移除 name 变量对应的值两边的空格，并输入移除后的内容
print(name.strip())
#     b.  判断 name 变量对应的值是否以  "al"  开头，并输出结果
print(name.strip().startswith('al'))
#     c.  判断 name 变量对应的值是否以  "X"  结尾，并输出结果
print(name.strip().endswith('X'))
#     d.  将 name 变量对应的值中的  “l”  替换为  “p”，并输出结果
print(name.strip().replace('l','p'))
#     e.  将 name 变量对应的值根据  “l”  分割，并输出结果。 
print(name.strip().split('l'))
#     f.  请问，上一题  e  分割之后得到值是什么类型（可选）？
print(type(name.strip().split('e')))
#     g.  将 name 变量对应的值变大写，并输出结果
print(name.strip().upper())
#     h.  将 name 变量对应的值变小写，并输出结果
print(name.strip().lower())
#     i.  请输出 name 变量对应的值的第 2 个字符？
print(name.strip()[1])
#     j.  请输出 name 变量对应的值的前 3 个字符？
print(name.strip()[0:3])
#    	  k.  请输出 name 变量对应的值的后 2 个字符？
print(name.strip()[-2:])
#     l.  请输出 name 变量对应的值中  “e”  所在索引位置？
print(name.strip().index('e'))
#     m.  获取子序列，仅不包含最后一个字符。如：  oldboy  则获取  oldbo;  root  则获取  roo
print(name.strip()[0:-1])

# 字符串是否可迭代对象？如可以请使用 for 循环每一个元素？
for i in name.strip():
	print(i,end = '+')
print()

# 请用代码实现：
#     a.  利用下划线将列表的每一个元素拼接成字符串，li  ＝  "alexericrain"
li = 'alexricrain'
print('_'.join(li))
#     b.  利用下划线将列表的每一个元素拼接成字符串，li  ＝  ['alex',  'eric',  'rain']    （可选）
li = ['alex','eric','rain']
print('_'.join(li))
"""
# Python2 中的 range 和 Python3 中的 range 的区别？
"""
python2中range会生成一个序列
python3中range会生成一个迭代器
"""

# 实现一个整数加法计算器：
#     如：
#     content  =  input('请输入内容：')    #  如：  5+9  或  5+  9  或  5  +  9  
"""
def add():
	n1 = input()
	n2 = input()
	print(int(n1) + int(n2))

add()
"""

# 计算用户输入的内容中有几个十进制小数？几个字母？
#     如：
#         content  =  input('请输入内容：')    #  如：asduiaf878123jkjsfd-­‐213928  
"""
content = input()
alpha = 0
num = 0
for i in content:
	if i.isalpha():
		alpha += 1
	if i.isdigit():
		num += 1
print(alpha,' ',num)
print()
"""

# 简述  int  和  9  等数字   以及   str  和  "xxoo"  等字符串的关系？
"""
int是类，9是具体对象
str是类，xxoo是具体对象
"""

# 制作趣味模板程序
#     需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
#          
#          如：敬爱可亲的 xxx，最喜欢在 xxx 地方 xxx
"""
template = "敬爱可亲的{},最喜欢在{}地方{}"
li = []
for i in range(3):
	s = input()
	li.append(s)
t = template.format(li[0],li[1],li[2])
print(t)
"""

# 制作随机验证码，不区分大小写。
#     流程：
#         -­‐  用户执行程序
#         -­‐  给用户显示需要输入的验证码
#         -­‐  用户输入的值
#             用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入
#         生成随机验证码代码示例：
"""
def check_code():
	checkcode = ''
	for i in range(4):
		current = random.randrange(0,4)
		if current != i:
			temp = chr(random.randint(65,90))
		else:
			temp = random.randint(0,9)
		checkcode += str(temp)
	return checkcode

while True:
	code = check_code()
	print(code)
	s = input('enter the code')
	if s == code:
		break
"""

# 开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
#     如  "苍老师"  "东京热"，则将内容替换为  ***
"""
s = input()
#if s.find('苍老师') != (-1):
if '苍老师' in s:
	v = s.replace('苍老师','*')
if s.find('东京热') != -1:
	v = s.replace('东京热','***')

print(v)
"""

# 制作表格  
#     循环提示用户输入：用户名、密码、邮箱  （要求用户输入的长度不超过 20 个字符，如果超过则只有前 20 个字符有效）
# 如果用户输入  q 或 Q  表示不再继续输入，将用户输入的内容以表格形式打印

s = ""
while True:
	f = input("q is quit")
	if f == 'q':
		break
	name = input()
	pswd = input()
	mail = input()
	template = "{}\t{}\t{}\t\n"
	t = template.format(name,pswd,mail)
	s = s + t

print(s.expandtabs(20))
