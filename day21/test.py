#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 从多层嵌套中一次退出，使用tag作为标识符

tag = True

while tag:
	s = input("input something access to next level: ")
	print('level1: %s ' % s)
	if s == 'quit':
		break
	if s == 'quit_all':
		tag = False
	while tag:
		s = input("input something access to next level: ")
		print('level2: %s ' % s)
		if s == 'quit':
			break
		if s == 'quit_all':
			tag = False
		while tag:
			s = input("input something access to next level: ")
			print('level3: %s ' % s)
			if s == 'quit':
				break
			if s == 'quit_all':
				tag = False
