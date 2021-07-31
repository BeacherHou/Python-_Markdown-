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


# 替代方案 A
# def file_scanner(fn_str, function):
# 	# 使用文件迭代器逐行扫描
# 	for line_str in open(fn_str, 'r'):
# 		# 调用一个函数对象
# 		function(line_str)


# 替代方案 B
# def file_scanner(fn_str, function):
# 	# 使用map代替了for循环
# 	list(map(function, open(fn_str, 'r')))


# 替代方案 C
# def file_scanner(fn_str, function):
# 	# 使用列表解析代替for循环
# 	[function(line_str) for line_str in open(fn_str, 'r')]


# 替代方案 D
# def file_scanner(fn_str, function):
# 	# 使用列表解析代替for循环
# 	list(function(line_str) for line_str in open(fn_str, 'r'))
