#!/usr/bin/env python


def file_scanner(fn_str, function):
	"通用文件扫描例行函数"

	file = open(fn_str, 'r')					# 创建文件对象

	while True:
		line_str = file.readline()				# 调用文件方法
		if not line_str:
			break								# 直到文件末尾
		function(line_str)						# 调用一个函数对象

	file.close()
