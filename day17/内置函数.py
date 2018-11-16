#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 常用的内置函数

# 绝对值abs()
print(abs(-3))

# all()对序列中每个元素做布尔运算，一个元素为False则为False
print(all([1,2,'1',None]))

# any()和all()相反，序列中有一个为真，则为真
print(any([1,None]))

# bin()计算二进制
print(bin(3))

# bytes()将字符以字节方式显示
print(bytes('女孩',encoding='utf-8'))
print(bytes('女孩',encoding='gbk'))

# chr()将数字转成字符,根据ascii码表
print(chr(999))

# divmod()将商和余数变成元组返回
print(divmod(10,3))

# eval()将字符串中数据结构提取出来，
dic = {'name':'alex'}
str_dic = str(dic)
d = eval(str_dic)
print(d)
s = '1+2*(3/3-1)-2'
print(eval(s))

# 可hash的数据类型就是不可变类型 , hash()显示对象的hash值
# 不管数据多长，hash值长度是固定的，不能根据hash值反推回原值
print(hash('hello'))

# globals()列出全局变量
print(globals())

# locals()列出局部变量
print(locals())

# zip()将参数一一对应组成元组，多余的抛弃，参数是序列(字符串，列表，元组)
res = zip(('a','b','c','d'),(1,2,3))
print(res)
print(list(res))

# max()和min()取最大和最小值
l = [1,3,100,-1,2]
print(max(l))
print(min(l))
# max(),min()高级应用,取出年龄最大的键值对
age_dic = {'age1':18,'age4':20,'age3':100,'age2':30}
#print(max(age_dic)) # 默认返回的是最大的键的值
res = zip(age_dic.values(),age_dic.keys())
res2 = list(res)
print(max(res2))


# 取值年龄最大的记录
people = [
	{'name':'alex','age':1000},
	{'name':'wupeiqi','age':10000},
	{'name':'yuanhao','age':9000},
	{'name':'linhaifeng','age':18}
]
print(max(people,key = lambda dic : dic['age']))


