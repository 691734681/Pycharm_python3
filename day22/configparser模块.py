#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# configparser模块是用来处理配置文件的，模式类似于字典
import configparser

config = configparser.ConfigParser() #创建configParser类对象


"""
# 查
config.read('config.ini') # 读取配置文件
print(config.sections()) # 不会返回 default
# 遍历配置文件
for i in config:
    for j in config[i]: # 每一层的遍历都会将defaut中的内容打印一遍
        print(j,' = ',config[i][j])
"""

"""
# 创建配置文件
config['mysql'] = {'user':'root','password':'123456'}
config['oracle'] = {'user':'scott','password':'tiger'}
config.write(open('dbconf.ini','w'))
"""
