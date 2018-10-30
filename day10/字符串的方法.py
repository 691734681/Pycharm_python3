#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

test = "aLex_alex"

# 首字母大写
v = test.capitalize()
print(v)

# 将字符串变小写，upper类似，变大写
v = test.casefold() # 较少使用
print(v)
v = test.lower()
print(v)

# 字符串居中，设置宽度，并且可以填充两边
print(test.center(20,'*'))  # 填充值是可选参数

# 字符串靠做，设置宽度，不足部分填充，rjust类似
print(test.ljust(20,'*'))

# 统计字符在字符串中出现的次数
print(test.count('a'))
# 并且可以指定查找的起始位置
print(test.count('a',2,3))

# encode
# decode

# 判断字符串以什么结尾
print(test.endswith("x"))
# 并且可以指定起始位置
print(test.endswith('L',0,2))

# 判断字符串以什么字符开头，可以指定起始位置
print(test.startswith('a',0))

# 找到字符串中指定的内容，返回第一次找到的值，可以指定起始位置
print(test.find('ex',5))

# 格式化字符串
test = 'I am {name}, I am {age}'
print(test.format(name = 'alex', age = 19))
test = 'I am {0}, I am {1} '
print(test.format('tom',28))

# 格式化字符串，使用字典
test = 'I am {name}, I am {age}'
print(test.format_map({'name':'sam','age':29}))

# 按照内容返回索引，如果没有则报错
test = 'alex_alex'
print(test.index('x'))

# 判断字符串是否只由字母和数字组成
test = 'uasf890+'
print(test.isalnum())

# 六个字符为一组，如果有tab则不足六个的组由tab补全
test = 'abcdefg\thijklm\tnops'
print(test.expandtabs(6))
s = 'username\temail\tpassword\nlaiying\tlaiying@qq.com\t123\nlaiying\tlaiying@qq.com\t123'
table = s.expandtabs(20)
print(table)

# 判断字符串是否只有字母
test = 'abcd'
print(test.isalpha())

# 判断字符串只有数字
test = "123"
print(test.isdigit())

# 字符串中大写变小写，小写变大写
test = 'AlEx'
print(test.swapcase())

#安行分割，布尔值表示是否保留换行符
test = 'asdfadfasdf\nasdfasdf\nadfasdf'
print(test.splitlines(True))

# 判断标识符是否正确，即变量命名规则是否正确
test = '123'
print(test.isidentifier())

# 判断字符串是否可打印，若有不可见字符，例如 \t
test = 'ab\tcd'
print(test.isprintable())

# 判断字符是标题
test = 'Alex'
print(test.istitle())

# 将指定参数作为，字符串中的字符的连接符，test须是可迭代的
test = '你是风儿我是沙'
print('_'.join(test))

# 删除空格，lstrip,rstrip删除左右空格
test = '  alex   '
print(test.strip())
# 也可以指定删除字符
test = 'abtttttab'
print(test.strip('ab'))

# maketrans translate一起用，创建对应表，置换对应的字符
test = 'aeiou'
test1 = '12345'
m = str.maketrans(test,test1)
v = 'abebibobub'
print(v.translate(m))

# 按指定分割符，分割字符串
test = 'testasdsddfg'
print(test.partition('s')) # 分割字符串，默认分3段中间段是指定的分割符
print(test.rpartition('s'))
print(test.split('s',2)) # 可以指定分割次数
print(test.rsplit('s'))

# 替换
test = 'alexalexalex'
print(test.replace('ex','bbb'))
print(test.replace('ex','bbb',2)) #指定替换次数

# 常用7个方法
"""
join(); split(); find(); strip(); upper(); lower(); replace()
"""

