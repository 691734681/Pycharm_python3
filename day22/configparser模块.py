#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# configparser模块是用来处理配置文件的，模式类似于字典
import configparser

config = configparser.ConfigParser() #创建configParser类对象

# 增
config.read('dbconf.ini')
config.add_section('Access')
config.set('Access','user','admin')
config.write(open('dbconf.ini','w'))

"""
# 删
config.read('dbconf.ini')
config.remove_section('sqlserver') # 删除指定的名字的第一层所有内容
config.remove_option('oracle','test') # 删除指定层下的指定键值对
config.write(open('dbconf.ini','w'))
"""

"""
# 改
config.read('dbconf.ini')
for i in config:
    if i == 'DEFAULT':
        continue
    for j in config[i]:
        if j == 'user':
            continue
        else:
            #config[i][j] = 'admin' 
            config.set(i,j,'admin') # 和上面一句作用相同，使用set方法，第一参数是第一层的key,第二个参数是第二层的key

config.write(open('dbconf.ini','w'))
"""

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
