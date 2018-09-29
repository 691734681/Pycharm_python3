#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

test = "charACter"

# 判断字符串是否只有字母和数字
v = test.isalnum()
print(v)

# 判断字符串是否是纯字母
v = test.isalpha()
print(v)

# 判断字符串是否是数字
test1 = "123"
v = test1.isdecimal()
print(v)
v = test1.isdigit()
print(v)
v = test.isnumeric()
print(v)

# 字符串中大小写字母互换
v = test.swapcase()
print(v)

# 判断字符串是小写
v = test.islower()
print(v)

# 判断字符串是空格组成的
v = test.isspace()
print(v)

# 判断字符串是否是标题（每个单词首字母大写）
v = test.istitle()
print(v)

# 将字符串变成标题格式
test1 = "return null if no result"
v = test1.title()
print(v)

# 在相邻字符间插入指定字符
test1 = "两江总督欢迎你"
t = "= "
v = t.join(test1)
print(v)

# 指定字符串长度，不足部分，用指定字符串在左边补足
v = test.ljust(20, "*")
print(v)

# 指定字符串长度，不足部分，用指定字符串在右边补足
v = test.rjust(20, "*")
print(v)

# 去除字符串两边及中间的空格，还可以去除指定字符
test1 = "  alex   "
v = test1.lstrip()
print(v)
v = test1.rstrip()
print(v)
v = test1.strip()
print(v)
test1 = "asalex"
v = test1.lstrip("a")
print(v)
v = test1.rstrip("x")
print(v)
v = test1.strip("a")
print(v)

# maketrans指定字符串中的字符的对应关系，translate将指定字符串的字符按照之前的对应关系替换
test1 = "aeiou"
test2 = "12345"
m = str.maketrans(test1, test2)
v = "abcedfghijklmnopqrstuvwxyz"
new_v = v.translate(m)
print(new_v)

# 按照指定的字符或字符串分割，只分割一次(包含分割的字符串)
test1 = "testasdsddfg"
v = test1.partition("s")
print(v)
v = test1.rpartition("s")
print(v)

# 按照指定的字符串，分割完（或分割指定次数）（不包含分割的字符串）
test1 = "testasdsddfg"
v = test1.split("s")
print(v)
v = test1.rstrip("s")
print(v)

# 按照换行符分割（True分割后包含换行符，False不包含）
test1 = "abcd\nefgh\nijkl\nmnop"
v = test1.splitlines(True)
print(v)
v = test1.splitlines(False)
print(v)

# 替换（可以指定替换次数）
test1 = "alexalexalex"
v = test1.replace("ex", "bb")
print(v)
