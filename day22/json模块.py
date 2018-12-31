#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# json模块用于数据传输(可以在不同语言间传输)
import json

dic = {'num':8,3:['a','b']} # json解析字典时，字典的键不能使用元组

"""
dumps和loads配对使用，dumps是将数据变成json字符串；loads是以json方式将数据从文件中读取
"""
# 将数据以json格式写入文件
# dic_str = json.dumps(dic)
# print(type(dic_str),' * ',dic_str)
# f_write = open('test.txt','w')
# f_write.write(dic_str)
# f_write.close()
# 将数据从文件中读出，并还原到原来的类型
# f_open = open('test.txt')
# data = f_open.read()
# print(type(data),' * ',data)
# f_open.close()
# data_dic = json.loads(data)
# print(type(data_dic),' * ',data_dic)

"""
dump和load配对使用，dump是将数据变成json字符串；load是以json方式将数据从文件中读取，使用方法和dumps,loads略有不同
"""
# 将数据以json格式写入文件
# f_write = open('test.txt','w')
# json.dump(dic,f_write)
# f_write.close()
# 将数据从文件中读出，并还原到原来的类型
f_read = open('test.txt')
data_dic = json.load(f_read)
print(type(data_dic),' * ',data_dic)