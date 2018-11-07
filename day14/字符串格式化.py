#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 百分号格式化字符串
# 参数可以是元组，不能是列表
"""
%s 可以接收所有类型
%d 只能接收数字
"""
print('i am %s my hobby is %s' %  ('alex','av'))

# 浮点数的拼接，默认保留六位，.2指定保留小数位
print('percent %.2f%s ' % (99.97,'%'))
print('percent %.2f%% ' % 99.97)

# 通过字典
tp1 = 'i am %(name)s age %(age)d' % {'name':'alex','age':30}
print(tp1)



# format格式化字符串
tp1 = 'i am {},age {}'.format('alex',37)
print(tp1)
tp1 = 'i am {1},age {0}'.format(38,'alex')
print(tp1)
tp1 = 'i am {name},age {age}'.format(name = 'alex',age = 41)
print(tp1)
tp1 = 'i am {name},age {age}'.format(**{'name':'alex','age':89})
print(tp1)


