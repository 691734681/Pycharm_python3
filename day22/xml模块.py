#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# xml模块
import xml.etree.ElementTree as ET

# 解析xml
#tree = ET.parse("xml_lesson")
# 得到根节点
#root = tree.getroot()
# 节点的tag(标签),attrib(属性),text(值)
#print(root.tag)
#print(type(root))
# print(root.attrib)
# print(root.text)
#print("#" * 50)

# 变量整个xml
# for i in root:
# 	print(i.tag," ",i.attrib," ",i.text)
# 	for j in i:
# 		print("    ",j.tag," ",j.attrib," ",j.text)
# 	print("#"*50)


# 遍历rank节点，通过节点下的iter()方法获取具体节点
# for node in root.iter("rank"):
# # 	print(node.tag," ",node.attrib," ",node.text)


# 修改xml (将year节点中的年份加1，并给year添加属性updated)
# for node in root.iter("year"):
# 	temp = int(node.text) + 1
# 	# 将新的值赋给node.text
# 	node.text = str(temp)
# 	# 添加updated属性
# 	node.set("updated","yes")
# 保存修改好的文件
# tree.write("xml_lesson")

# 删除xml内容
# for country in root.findall("country"):
# 	rank = int(country.find("rank").text)
# 	if rank > 50:
# 		root.remove(country)
# 将改好的文件写入xml_bak
# tree.write("xml_bak.xml")


# 创建一个xml文档
# 创建一个根节点(namelist)
namelist = ET.Element("namelist")
# 创建子节点 (四个参数分别是：父节点标签，自己的标签名，属性)
name = ET.SubElement(namelist,"name",attrib={"enrolled":"true"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
age.text = "10"
gender = ET.SubElement(name,"gender")
gender.text = "male"

name2 = ET.SubElement(namelist,"name",attrib={"enrolled":"true"})
age = ET.SubElement(name2,"age",attrib={"checked":"no"})
age.text = "20"
gender = ET.SubElement(name2,"gender")
gender.text = "female"

# 生成xml文档对象
et = ET.ElementTree(namelist)
# 保存到xml文件
et.write("new_xml.xml",encoding="utf-8",xml_declaration="true")


