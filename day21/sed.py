#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import os

l = [{"backend": "www.oldboy1.org", "record": {"server": "2.2.2.4", "weight": 20, "maxconn": 3000}},
	 {"backend": "www.oldboy1.org", "record": {"server": "10.10.0.10", "weight": 30, "maxconn": 4000}}]


# 对haproxy增删改查
def query(data):
	print("这是查询功能")
	# print("用户输入的数据是：%s" % data)
	backend_data = "backend %s" % data
	# print(backend_data)
	#res = []
	with open("haproxy.conf") as read_f:
		res = []
		tag = False
		for read_line in read_f:
			# print(read_line, end="")
			if read_line.strip() == backend_data:
				tag = True
				continue
			if tag:
				if read_line.startswith("backend"):
					break
				res.append(read_line)
				print(read_line, end="")
	return res


def add():
	print("这是添加功能")


def update(data):
	print("这是修改功能")
	print("用户输入的数据是：", data)
	backend = data[0]["backend"]
	res = query(backend)
	print("修改前的列表",res)
	backend_data = "backend %s" % backend
	#print(backend_data)
	#print("来自update函数：", res)
	if not res:
		return "你要修改的记录不存在"
	#        server 2.2.2.4 weight 20 maxconn 3000
	old_server_record = "%sserver %s weight %s maxconn %s\n" % (
		' ' * 8, data[0]["record"]["server"], data[0]["record"]["weight"], data[0]["record"]["maxconn"])
	#print("你想要修改的数据是：", old_server_record)
	if old_server_record not in res:
		return "你要修改的记录不存在"
	index = res.index(old_server_record)
	print(index)
	new_server_record = "%sserver %s weight %s maxconn %s\n" % (
		" " * 8, data[1]["record"]["server"], data[1]["record"]["weight"], data[1]["record"]["maxconn"])
	#print("新的记录", new_server_record)
	res[index] = new_server_record
	print("修改后的列表",res)
	with open("haproxy.conf") as read_f,open("new_haproxy.conf","w") as write_f:
		tag = False
		has_write = False
		for read_line in read_f:
			if read_line.strip() == backend_data:
				tag = True
				write_f.write(read_line)
				continue
			if tag and read_line.startswith("backend"):
				tag = False
			if not tag:
				write_f.write(read_line)
			else:
				if not has_write:
					for record in res:
						print("循环中的值:",record)
						write_f.write(record)
						has_write = True
	os.rename("haproxy.conf","haproxy.conf.bak")
	os.rename("new_haproxy.conf","haproxy.conf")
	#os.remove("haproxy.conf.bak")


def delete():
	print("这是删除功能")


if __name__ == "__main__":
	# print("test")
	msg = """
	请选择功能：
	1：查询
	2：添加
	3：修改
	4：删除
	5：退出
	"""
	msg_dic = {
		"1": query,
		"2": add,
		"3": update,
		"4": delete
	}

	while True:
		print(msg)
		choice = input("请输入你的选项：").strip()
		if not choice:
			continue
		if choice == "5":
			break
		data = input("请输入你的数据：").strip()
		# 将输入的字符串转成列表
		if choice != "1":
			data = eval(data)
		res = msg_dic.get(choice)(data)
		print(res)
