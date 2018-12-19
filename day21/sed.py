#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 对haproxy.conf文件的增删改查

# 查询
def fetch(data):
	print('这是查询功能：')
	with open('haproxy.conf') as read_f:
		flag = False
		res = []
		for read_line in read_f:
			# print(read_line,end = '')
			if read_line.strip() == data:
				flag = True
				continue
			if flag:
				if read_line.startswith(' '):
					print(read_line,end = '')
					res.append(read_line)
				else:
					flag = False
	return res

# 添加
def add(data):
	print('这是增加功能：')


# 更改
def change(data):
	print('这是更改功能：')

# 删除
def delete(data):
	print('这是删除功能')


if __name__ == '__main__':
	msg = """
	**********
		1.查询
		2.添加
		3.修改
		4.删除
		5.退出
	**********
	"""

	msg_dic = {
		'1':fetch,
		'2':add,
		'3':change,
		'4':delete
	}

	while True:
		print(msg)
		choice = input('请输入你的选项: ').strip()
		if not choice:
			print('你没有输入任何内容，请继续')
			continue
		if choice == '5':
			break

		data = input('输入你要查询/添加/修改/删除的内容: ')

		res = msg_dic[choice](data)
		print(res)