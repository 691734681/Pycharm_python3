#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import requests
import json

r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=115.239.211.112')

print(r.text)
print(json.dumps(r.json(),ensure_ascii = False, indent = 5))
