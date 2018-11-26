#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 用户列表
user_list = [
	{'name':'alex','passwd':'123'},
	{'name':'linhaifeng','passwd':'123'},
	{'name':'wupeiqi','passwd':'123'},
	{'name':'yuanhao','passwd':'123'}
]

# 当前登录用户的信息
current_dic = {'name':None,'login':False}

# 装饰器 --- (给装饰器加参数)
def auth(auth_type = 'filedb'):
	def auth_func(func):
		def wrapper(*args,**kwargs):
			print(auth_type)
			if auth_type == 'filedb':
				#如果用户已经登录过了，则直接运行被修饰的程序
				if current_dic['name'] and current_dic['login']:
					res = func(*args,**kwargs)
					return res
				#如果用户还没登录，则输入用户名和密码
				username = input('输入用户名：')
				password = input('输入密  码：')
				# 通过用户列表验证
				for user_dic in user_list:
					if user_dic['name'] == username and user_dic['passwd'] == password:
						current_dic['name'] = username
						current_dic['login'] = True
						res = func(*args,**kwargs)
						return res
				else:
					print('用户名或密码错误')
			elif auth_type == 'ldap':
				print('不知道ldap怎么玩')
			else:
				print('不知道你是什么验证类型')
		return wrapper
	return auth_func


# 上面的装饰器为下面的函数为添加验证功能
# 这里装饰器需要加()运行，这样返回auth_func装饰器
@auth()
def index():
	print('欢迎来到京东主页')

@auth('ldap')
def home(name):
	print('欢迎回家%s' % name)

@auth('nothing')
def shopping_car(name):
	print('%s购物车里有[%s,%s,%s]' % (name,'奶茶','妹妹','娃娃'))

def order():
	print()


index()
home('产品经理')
shopping_car('产品经理')



