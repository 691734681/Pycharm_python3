#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 字符串常用方法的演示

test = "charACter"

# 首字母大写
v = test.capitalize()
print(v)

# 所有字母小写
v = test.lower()
print(v)

# 所有字母大写
v = test.upper()
print(v)

# 整个字符串占10个位置，不足用+补足，而且字符串居中
v = test.center(10, "+")
print(v)

# 计算指定字符或字符串出现的次数
v = test.count("a")
print(v)

# 是否以指定字符或字符串结尾
v = test.endswith('x')
print(v)

# 是否以指定字符或字符串开头
v = test.startswith("a")
print(v)

# 查找指定字符或字符串的位置
v = test.find("ar")
print(v)

# 使用指定的字符或数字填充
test1 = "i am {name}, age {a}"
test2 = "i am {0}, age {1}"
v = test1.format(name="alex", a=19)
print(v)
v = test2.format("alex", 20)
print(v)

# 查找指定字符或字符串
v = test.index("ar")
print(v)

