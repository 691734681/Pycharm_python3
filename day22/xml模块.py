#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import xml.etree.ElementTree as ET

"""
# 遍历xml文档
tree = ET.parse('test.xml')  # 解析xml文档获取树对象
root = tree.getroot() # 获取根对象
print(root.tag) # 打印根标签

for i in root:
    print(i.tag,' * ',i.attrib)
    for j in i:
        print('    ',j.tag,' * ',j.attrib,' * ',j.text)
"""




"""
# iter()方法返回root下所有节点，可以直接遍历所有节点元素

# # 循环遍历root
# def view_xml(root):
#     for i in root.iter():
#         print(i.tag,' * ',i.attrib,' * ',i.text)
#
# view_xml(root)
"""











