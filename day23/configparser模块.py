#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# configparser模块
import configparser

"""
# 生成一个配置文件
# 生成一个config对象
config = configparser.ConfigParser()
# 将文件以键值对形式表示
config["DEFAULT"] = {
	"ServerAliveInterval": 45,
	"Compression": "yes",
	"CompressionLevel": 9,
	"ForwardX11": "yes",
}

config["bitbucket.org"] = {"User": "hg"}

config["topsecret.server.com"] = {
	"Port": 50022,
	"ForwardX11": "no"
}

# 打开要写入的文件，并获得句柄
with open("example.ini", "w") as f_write:
	# 使用config对象中的写方法
	config.write(f_write)
	

# 配置文件的查找
# 获取config对象
config = configparser.ConfigParser()
# 关联配置文件
config.read("confile") # 获取default以外的块名
print(config.sections())

"""

config = configparser.ConfigParser()
config.read("confile")

# 增加
# 添加块
config.add_section("yuan")
#config.add_section("alex")
# 添加块下的键值对
config.set("yuan","key","value")
# config.set("alex","gender","male")


# 删除
# 删除块
config.remove_section("yuan")
# 删除块下的键值对
config.remove_option("alex","gender")


# 将修改好的数据写入文件
with open("confile","w") as f_write:
	config.write(f_write)
