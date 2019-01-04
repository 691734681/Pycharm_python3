#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# logging 模块用于记录日志
import logging


# logging第一种用法 （较少用）
'''
logging模块通过调用basicConfig方法配置打印的各种信息及格式
level表示打印的级别，默认是warning
format表示打印需要打印的内容，asctime表示时间（有默认的格式），name表示用户（root)，lineno表示执行打印的代码所在的行，message表示打印的信息
filename表示将打印的内容输出到指定文件，如果没有filename这项，则默认将打印输出的控制台
filemode表示文档的输出模式和操作文件的模式是一样的
datefmt表示输出日期的模式，可以自定义
'''
# logging.basicConfig(
#     level = logging.DEBUG,
#     format= '%(asctime)s  %(name)s  %(lineno)d  %(message)s',
#     filename = 'log_1.log',
#     filemode = 'a',
#     #datefmt= '%Y  %m  %D'
#     datefmt = '%a, %d %b %Y %H:%M:%S'
# )
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# -------------------------------------------------------------


# logging的第二种用法（较常用）
# logger = logging.getLogger()  # 创建logger对象
# logger.setLevel(logging.DEBUG) # 设置logger级别
#
# fh = logging.FileHandler('log_2.log','w')  # 创建输出到文件的handler
# sh = logging.StreamHandler() # 创建输出到控制台的handler
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 设置输出格式
#
# fh.setFormatter(formatter) # 将输出格式添加到handler
# sh.setFormatter(formatter) # 将输出格式添加到handler
#
# logger.addHandler(fh) # 将handler添加到logger对象
# logger.addHandler(sh) # 将handler添加到logger对象
#
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')

#---------------------------------------------------------------

# 多个logger时的输出
"""
logger,logger2,logger3是一级一级的继承关系，logger默认是root，logger直接命名是root的子，logger3是son的子
多个logger中，最顶层父辈只输出一次，子级在第几层就输出几次，例如logger2有一个父辈root所以输出2次，logger3输出三村
"""
# logger = logging.getLogger()
# logger.setLevel('DEBUG')
#
# logger2 = logging.getLogger('son')
# logger2.setLevel('WARNING')
#
# logger3 = logging.getLogger('son.grandson')
# logger3.setLevel('CRITICAL')
#
# fh = logging.FileHandler('log_3.log','w')
# sh = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# fh.setFormatter(formatter)
# sh.setFormatter(formatter)
#
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# logger2.addHandler(fh)
# logger2.addHandler(sh)
#
# logger3.addHandler(fh)
# logger3.addHandler(sh)
#
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')
#
# logger2.debug('debug')
# logger2.info('info')
# logger2.warning('warning')
# logger2.error('error')
# logger2.critical('critical')
#
# logger3.debug('debug')
# logger3.info('info')
# logger3.warning('warning')
# logger3.error('error')
# logger3.critical('critical')

#-------------------------------------------------

logger = logging.getLogger()
logger.setLevel('DEBUG')

logger2 = logging.getLogger('son')
logger2.setLevel(logging.WARNING)

fh = logging.FileHandler('log_4.log','w')
sh = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
sh.setFormatter(formatter)

"""
创建过滤器是如果没有参数，则什么都不过滤
参数就是创建的logger的名字，过滤器过滤掉不是参数名字的logger所打印的信息
"""
f = logging.Filter('son')  # 创建过滤器 # 名字为son的logger会打印出信息
fh.addFilter(f)   # 将过滤器添加到handler
sh.addFilter(f)

logger.addHandler(fh)
logger.addHandler(sh)

logger2.addHandler(fh)
logger2.addHandler(sh)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

logger2.debug('debug')
logger2.info('info')
logger2.warning('warning')
logger2.error('error')
logger2.critical('critical')
