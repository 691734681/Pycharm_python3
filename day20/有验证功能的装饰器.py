#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-


# 要求调用每个函数时都要验证是否登录
def auth_func(func):
	def login(*args, **kwargs):
		username = input("输入用户名：").strip()
		password = input("输入密码：").strip()
		if username == "sb" and password == "123":
			res = func(*args, **kwargs)
			return res
		else:
			print("用户名或密码不正确")

	return login


# 给下面所有的函数加上一个装饰器
@auth_func
def index():
	print("欢迎来到京东主页")


@auth_func
def home(name):
	print("欢迎回家%s" % name)


@auth_func
def shopping_car(name):
	print("%s购物车里有[%s,%s,%s]" % (name, "奶茶", "妹妹", "娃娃"))

home("sb")