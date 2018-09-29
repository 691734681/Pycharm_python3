#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 字符串格式化的演示 %s 表示字符串
msg = "i am %s my hobby is alex"
print(msg % "lhf")

# 传多个字符串，多个传入的字符串用括号括起来，（传元组也可以，列表不行）
msg = "my hobby is %s, %s"
print(msg % ("reading", "cooking"))
t = ("football", "basketball")
print(msg % t)

# %d表示的是串入的是整数
msg = "i am %s , age %d"
name = "sam"
age = 36
print(msg % (name, age))

# $f表示浮点数(.2表示保留2位小数)
msg = "percent %.2f"
print(msg % 99.23423)

# 打印百分号
msg = "percent %.2f%%"
print(msg % 99.36548)

# 使用字典传值
msg = "i am %(name)s , age is %(age)d"
print(msg % {"name": "alex", "age": 18})

# 打印分割符
print("root", "x", "0", "0", sep=":")

tp = "i am {}, age{}".format("seven", 18)
print(tp)

# 使用列表传值 (元组传值和列表一样)
tp = "i am {}, age {}".format(*["seven", 18])
print(tp)

# 使用字典传值
tp = "i am {name},age {age}".format(**{"name": "seven", "age": 18})
print(tp)