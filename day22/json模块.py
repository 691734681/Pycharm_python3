#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# json模块 : 将各种数据类型转换为json格式并写入文件
import json

# 将数据转换成json类型，使用json.dumps
dic = {"name": "alex"}
data = json.dumps(dic)
print(data)
print(type(data))
# 将json数据类型转换回来，使用json.loads
dic2 = json.loads(data)
print(dic2)
print(type(dic2))

print("#" * 50)

# （dumps,loads）对应（dump,load）
# 第1组可以单单转换，也可以写入文件
# 第2组只能写入文件时使用

l = [11, 12]
# 第1组写入文件实例
# 将数据转换成json格式并写入文件
data = json.dumps(l)
f_write = open("dumps", "w")
f_write.write(data)
f_write.close()
# 将数据读取出来，并还原成原来的格式
f_read = open("dumps")
data2 = json.loads(f_read.read())
f_read.close()
print(data2)
print(type(data2))

l2 = [33, 44]
# 第2组写入文件实例
# 将数据转换成json格式并写入文件
f_write2 = open("dump", "w")
json.dump(l2, f_write2)
f_write2.close()
# 将数据读取出来，并还原成原来的格式
f_read2 = open("dump")
data3 = json.load(f_read2)
f_read2.close()
print(data3)
print(type(data3))
