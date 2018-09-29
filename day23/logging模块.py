#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# logging模块
import logging

# 调整level级别，log写入的文件
# logging.basicConfig(
# 	level=logging.DEBUG,
# 	filename="logger.log",
# 	# 默认是追加模式
# 	#filemode = "w",
# 	#日志打印格式
# 	format = "%(asctime)s [%(lineno)d] %(message)s",
# 	# 日期格式
# 	#datefmt =
# )

# 日志级别 (系统默认level = warning) ，debug,info不显示
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")


# 使用logger对象

# 得到logger对象
logger = logging.getLogger()
# 设置logger显示的级别
logger.setLevel("DEBUG")
# 得到向文件和屏幕输出的对象
fh = logging.FileHandler("test.log")
sh = logging.StreamHandler()
# 设置输出格式
fm = logging.Formatter("%(asctime)s --- %(message)s")
# 将fm添加到fh,sh
fh.setFormatter(fm)
sh.setFormatter(fm)
# 将fh,sh添加到logger
logger.addHandler(fh)
logger.addHandler(sh)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

