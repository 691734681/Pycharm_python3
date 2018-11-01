#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 字典的键是除列表,字典外的任何值(即键不可以用可变元素)，值可以是任何值
# 字典是无序的
info = {'k1':18,2:True,'k3':[11,[],(),22,33,{'kk1':'vv1','kk2':'vv2','kk3':(11,22)}],'k4':(11,22,33,44)}
print(info)

# 字典的常见操作

# 取值
print(info['k3'][-1]['kk3'][0])
print(info.get('k1')) #key不存在时，返回None,也可以添加第二个参数指定默认值

# 删除
del info['k1']
print(info)
print(info.pop(2))
info.popitem() #随机删除一个键值对

# 循环 (对字典for循环默认就是循环key)
for item in info:
	print(item,end = ' ')
print()

for value in info.values():
	print(value,end = ' ')
print()

# 拷贝
info2 = info.copy()
print(info2)

# 清空字典
info.clear()
print(info)

# 生成字典
dic = dict.fromkeys(['k1',123,'999'],2) # 默认第二个参数是None
print(dic)

# 设置键值对 (如果键原来存在，不做任何事，仅返回原值，如果不存在设置新键值对，并返回新的键值对)
dic.setdefault('k1',888)
print(dic)

# 更新
dic.update({'k1':1000})
print(dic)
