#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

"""
# 执行python脚本的两种方式
# 1. python3 1.py  2. ./1.py


# 简述位，字节的关系
# 一个字节占8个byte位


# 简述ascii,unicode,utf-8,gbk的关系
#


# 请写出“李杰”分别用utf-8和gbk编码所占位数
# utf-8占6个字节，gbk占4个字节


# python单行注释和多行注释分别是什么
# 单行注释是“#”，多行注释是 “““ ”””或''' '''


# 声明变量注意事项
# 1. 变量由数字，字母，下划线组成
# 2. 数字不能开头
# 3. 不能使用Python关键字


# 如有下一变量n1=5，请使用Int提供的方法，得到该变量最少用多少个二进制位表示
n1 = 5
length = n1.bit_length()
print(length)


# 布尔值分别有什么
# True , False


# 阅读代码，写出执行结果
'''
a="alex"
b=a.capitalize()
print(a)
print(b)
'''
# a="alex",b="Alex"


# 写代码，有如下变量，请按照要求实现每个功能
name = " aleX"
# 移除name变量对应的值两边的空格，并输出移除后的内容
v = name.strip()
print(v)
# 判断name变量对应的值是否以“al”开头，并输出结果
v = name.startswith("al")
print(v)
# 判断name变量对应的值是否以“X”结尾，并输出结果
v = name.endswith("X")
print(v)
# 将name变量对应的值中的“l”替换为“p”，并输出结果
v = name.replace("l", "p")
print(v)
# 将name变量对应的值根据“l”分割，并输出结果
v = name.split("l")
print(v)
# 上一题，e分割之后得到的值是什么类型
# 列表
# 将name变量对应的值变小写，并输出结果
v = name.lower()
print(v)
# 将name变量对应的值变大写，并输出结果
v = name.upper()
print(v)
# 输出name变量对应的值的第2个字符
print(name[1])
# 输出name变量对应的值的前3个字符
print(name[0:3])
# 输出name变量对应的值的后2个字符
print(name[-3:-1])
# 输出name变量对应的值中“e”所在索引位置
v = name.index("e")
print(v)
# 获取子序列，仅不包含最后一个字符.
v = name[0:-1]
print(v)


# 字符串是否可迭代对象？如可以，请使用for循环每个元素
s = "abcdefghijklmnopqrstuvwxy"
for i in s:
	print(i)


# 请用代码实现
# 利用下划线将列表的每个元素拼接成字符串，
li = "alexericrain"
new_li = "_".join(li)
print(new_li)
# 利用下划线将列表的每个元素拼接成字符串，
li = ["alex", "eric", "rain"]
new_li = "_".join(li)
print(new_li)


# python2中的range和python3中的range的区别
# python2中range(10)后会立即生成10个数；python3则不会，而是使用时再生成


# 实现一个整数加法计算器
# 如 content=input【“请输入内容：”】 # 如： 5+9
def add():
	n1 = input("input a number：")
	n2 = input("input a number：")
	sum = int(n1) + int(n2)
	return sum


s = add()
print(s)


# 计算用户输入的内容中有几个十进制小数？几个字母
# 如 content=input('请输入内容：') 如：asduiaf878123jkjsfd-213928
s = "asduiaf878123jkjsfd-213928"
s_num = 0
i_num = 0
for i in s:
	temp = i
	if i.isalpha():
		s_num += 1
	if i.isnumeric():
		i_num += 1

print(s_num)
print(i_num)


# 简述int和9等数字以及str和“xxoo"等字符串的关系
# 9的类型是int，"xxoo"的类型是str


# 制作趣味模板
# 需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实1
# 如：敬爱可亲的xxx，最喜欢在xxx 地方干xxx
s = "敬爱可亲的{0}，最喜欢在{1}地方干{2}"
name = input("name:")
locale = input("locale:")
hobby = input("hobby:")
new_s = s.format(name, locale, hobby)
print(new_s)
"""

# 制作随机验证码，不区分大小写。
'''
流程：
‐ 用户执行程序
‐ 给用户显示需要输入的验证码
‐用户输入的值
用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入
生成随机验证码代码示例：
'''


def check_code():
	import random
	checkcode = ''
	for i in range(4):
		current = random.randrange(0, 4)
		if current != i:
			temp = chr(random.randint(65, 90))
		else:
			temp = random.randint(0, 9)
		checkcode += str(temp)
	return checkcode


while True:
	code = check_code()
	print(code)
	s = input("please put the code : ")
	s = s.upper()
	if s == code:
		break

"""
# 开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
# 如"苍老师""东京热"，则将内容替换为***
s = input("input something:")
if s.count("苍老师") != 0:
	s = s.replace("苍老师", "***")
if s.count("东京热") != 0:
	s = s.replace("东京热", "***")
print(s)


# 制作表格
# 循环提示用户输入：用户名、密码、邮箱 （要求用户输入的长度不超过20 个字符，如果超过则只有前20 个字符有效）
# 如果用户输入q 或Q 表示不再继续输入，将用户输入的内容以表格形式打印
s = "\t"
content = ""
while True:
	u = input("username : ")
	p = input("password :")
	e = input("email : ")
	if len(u) > 20:
		u = u[0:20]
	if len(p) > 20:
		p = p[0:20]
	if len(e) > 20:
		e = e[0:20]
	content = content + u + s + p + s + e + s + "\n"
	t = input("quit or not (q or Q mean quit):")
	if t == "q" or t == "Q":
		break

print(content.expandtabs(20))
"""
