#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import requests
import json
#
# ip = input("enter ip address:")
# url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
# print(url)
# r = requests.get(url)
# print(type(r.json()))
# print(json.dumps(r.json(),ensure_ascii = False,indent = 5))
# print(r.json()['data']['country'])

# data = dict(name='a_kui',email='a_kui@test.com')
# res = requests.post("http://httpbin.org/post",data = data)
# print(res.text)

# r = requests.get('http://httpbin.org/redirect/3')
# l = r.history
# print(l)
# for i in l:
#     print(i.url[18:])
# print(r.url[18:])

# print(json.dumps(r.json(),ensure_ascii=False,indent=5))

l = []
l.append('name1=sb1')
l.append('name2=sb2')
print(l)
s = '&'.join(l)
url = 'http://httpbin.org/cookies/set?'+s
print(url)
r = requests.get(url)
print(r.json())
