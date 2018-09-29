#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 写文件
# w模式：如果文件不存在，则建立新的文件；如果文件存在，则清空文件再写
f = open("test", "w")
print(f.readable())
print(f.writable())
f.write("111111\n")
f.write("222222\n")
f.write("333333\n444444\n555555\n")
f.writelines(["666666\n", "777777\n"])
f.close()


