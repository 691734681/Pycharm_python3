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

##############################################################

"""
# 修改文件
tree = ET.parse('test.xml')
root = tree.getroot()
for country in root.findall('country'):
    for i in country.iter('year'):
        year = int(i.text) + 1
        i.text = str(year)

tree.write('test2.xml')
"""

##############################################################

"""
# 删除元素
tree = ET.parse('test.xml')
root = tree.getroot()
for country in root.iter('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
            root.remove(country)

tree.write('test2.xml')
"""

##############################################################


# 创建xml
root = ET.Element('country')
city = ET.SubElement(root,'city',{'name':'beijing'})
year = ET.SubElement(city,'year')
year.text = '2018'
gdp = ET.SubElement(city,'gdp',{'checked':'yes'})
gdp.text = '10000'
city = ET.SubElement(root,'city',{'name':'shanghai'})
year = ET.SubElement(city,'year')
year.text = '2019'
gdp = ET.SubElement(city,'gdp',{'checked':'yes'})
gdp.text = '10001'
et = ET.ElementTree(root)
et.write('test2.xml')



##############################################################
"""
# iter()方法返回root下所有节点，可以直接遍历所有节点元素

# # 循环遍历root
# def view_xml(root):
#     for i in root.iter():
#         print(i.tag,' * ',i.attrib,' * ',i.text)
#
# view_xml(root)
"""











