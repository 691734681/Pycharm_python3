#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import re

ret = re.findall('abc{1,4}?','sfojewifoabcccc')
print(ret)