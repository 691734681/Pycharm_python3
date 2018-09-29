#!/usr/local/python3.5/bin/python3

# 使用while循环输出1,2,3,4,5,6,8,9,10
'''
n1=1
while n1<11:
	if n1!=7:
		print(n1)
	n1=n1+1
'''

# 求1-100的所有数的和
'''
n2=1
sum2=0
while n2<=100:
	sum2=sum2+n2
	n2=n2+1
print(sum2)
'''

# 输出1-100内所有奇数
'''
n3=1
while n3<=100:
	if n3%2==1:
		print(n3)
	n3=n3+1
'''

# 输出1-100内所有偶数
'''
n4=1
while n4<=100:
	if n4%2==0:
		print(n4)
	n4=n4+1
'''

# 求1-2+3-4+5-6+...+99的和

n5 = 1
sum5 = 0
while n5 < 100:
	if n5 % 2 == 0:
		sum5 = sum5 - n5
	else:
		sum5 = sum5 + n5
	n5 = n5 + 1
print(sum5)

# 用户登录（三次机会）
'''
count=1
while count<4:
	name=input("name: ")
	passwd=input("password: ")
	if name=='root' and passwd=='root':
		print('login')
		break;
	print('you can try 3 times')
	if count==3:
		print('you have no chance')
	else:
		print('this is the '+str(count)+' times')
	count=count+1
'''
