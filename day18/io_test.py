#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 以字节(b)方式打开文件，不能指定编码格式
# f = open("test", "rb")
# data = f.read()
# print(data)
# # 解码字节文件
# print(data.decode("utf8"))
# f.close()


f1 = open("test", "wb")
f1.write(bytes("55555\r\n", encoding="utf-8"))
f1.write("hello,世界\r\n".encode("utf-8"))
# tell方法提示当前光标所在位置
print(f1.tell())
# 移动光标位置
f1.seek(0)
print(f1.tell())
f1.close()


