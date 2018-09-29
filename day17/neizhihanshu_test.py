#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 内置函数的演示

# abs()取绝对值
print(abs(-2))

# all()参数是可迭代类型(序列)
# 如果序列中每个元素都是true则返回true
# 如果序列为空则返回true
print(all([1]))

# any()和all()相反，序列中有一个为true则返回true
print(any([0, 1]))

# bin()将十进制变二进制
print(bin(10))

# bool()返回boolean值
print(bool(0))
print(bool(""))
print(bool(None))

# bytes()将字符串变成字节
print(bytes("你好", encoding='utf-8'))
print(bytes("你好", encoding='utf-8').decode("utf-8"))
print(bytes("你好", encoding='utf-8').decode("gbk"))

# chr()按照ascii进行字符转换
print(chr(97))

# dir() 显示对象的属性和方法
print(dir(abs))

# divmod() 取商得余数
print(divmod(10, 3))

# enumerate()
print(enumerate("abc"))

# eval()将字符串中的数据结构提取出来或将字符表示的数学运算计算
print(eval("[1,2,3]"))
print(eval("1+2+3"))

# hash()得出数据hash值，可hash的就是不可变数据类型
print(hash("abc"))

# help()查询函数帮助

# id()对象内存地址

# input()接受输入

# int()将字符数字变成数字

# len()序列长度

# globals()显示系统的全局变量
print(globals())

# locals()显示当前级别的局部变量
print(locals())

age_dict = {"age1": 18, "age4": 20, "age3": 100, "age2": 30}
# min() 取最小值
res = zip(age_dict.values(), age_dict.keys())
print(min(res))
# max() 取最大值
res = zip(age_dict.values(), age_dict.keys())
print(max(res))

# zip() 将两个序列组成一个元组组成的列表，返回的是一个迭代器
res = zip(("a", "b", "c", "d"), (1, 2, 3))
print(res)
print(list(res))

p = {"name": "alex", "age": 18, "gender": "None"}
res = zip(p.keys(), p.values())
print(list(res))
print(list(res))

# ord() 将字符变成ascii表
print(ord("a"))

# pow() 几的几次方

# reversed() 反转序列，返回的是个迭代器
print(list(reversed([1, 2, 3, 4, 5])))

# round() 对小数四舍五入

# slice() 对序列进行切片
s = "hello"
s1 = slice(3, 5, 1)
print(s[s1])

# sorted() 排序，返回一个排好序的对象，不会影响原来的序列
li = [1, 4, 5, 3, 2, 6]
res = sorted(li)
print(res)
print(res)
print(li)

# sum() 求和

# tuple() 将序列变为元组

# type() 查看对象类型

# vars()
# 如果不传参数等同于locals()
print(vars())
# 如果传参数，就是查看对象所有方法
print(vars(str))

# __import__() 导入字符串类型的模块文件

