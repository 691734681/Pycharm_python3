#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

tag = True

# 如果没有tag的代码，就只能一层一层退出；加入含有tag的代码就可以一次退出

while tag:
	print("level1")
	choice = input("level1>> : ").strip()
	if choice == "quit":
		break
	if choice == "quit_all":
		tag = False
	while tag:
		print("level2")
		choice = input("level2>> : ").strip()
		if choice == "quit":
			break
		if choice == "quit_all":
			tag = False
		while tag:
			print("level3")
			choice = input("level3>> : ").strip()
			if choice == "quit":
				break
			if choice == "quit_all":
				tag = False


