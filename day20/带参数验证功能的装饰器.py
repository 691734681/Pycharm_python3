#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 使用全局变量记录用户的状态
current_user = {"username": None, "login": False}
# 定义存在的用户
user = [
	{"name": "alex", "passwd": "123"},
	{"name": "linhaifeng", "passwd": "123"},
	{"name": "wupeiqi", "passwd": "123"},
	{"name": "yuanhao", "passwd": "123"}
]


# 要求调用每个函数时都要验证是否登录
# 带参数的装饰器：就是在原来的装饰器上再加一层，利用闭包原理
def auth(auth_type):
	def auth_func(func):
		def login(*args, **kwargs):
			print(auth_type)
			if auth_type == "filedb":
				if current_user["username"] and current_user["login"]:
					res = func(*args, **kwargs)
					return res
				username = input("用户名：").strip()
				password = input("密  码：").strip()
				for user_dic in user:
					if user_dic["name"] == username and user_dic["passwd"] == password:
						current_user["username"] = username
						current_user["login"] = True
						res = func(*args, **kwargs)
						return res
				else:
					print("用户名或密码不正确")
			elif auth_type == "ldpa":
				print("不知道怎么玩")
				res = func(*args, **kwargs)
				return res
			else:
				print("鬼才知道怎么玩")
				res = func(*args, **kwargs)
				return res

		return login

	return auth_func


# 给下面所有的函数加上一个装饰器
@auth("filedb")
def index():
	print("欢迎来到京东主页")


@auth("ldpa")
def home(name):
	print("欢迎回家%s" % name)


@auth("test")
def shopping_car(name):
	print("%s购物车里有[%s,%s,%s]" % (name, "奶茶", "妹妹", "娃娃"))


index()
home("产品经理")
shopping_car("产品经理")
