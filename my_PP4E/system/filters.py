#!/usr/bin/env python


import sys


def filter_file(fn_str, function):
	"显示指定文件"

	input_file = open(fn_str, 'r')
	# 显示地指出输出文件
	output_file = open(fn_str + '.out', 'w')

	for line_str in input_file:
		output_file.write(function(line_str))

	input_file.close()
	output_file.close()


# 替代方案
# 利用上下文管理器
# def filter_file(fn_str, function):
# 	with open(fn_str, 'r') as input_file, open(fn_str + '.out', 'w') as output_file:
# 		for line_str in input_file:
# 			output_file.write(function(line_str))


def filter_stream(function):
	"利用标准输入/输出流允许在命令行中重定向"

	while True:
		line_str = sys.stdin.readline()	# 可替换为input()
		if not line_str:
			break
		print(function(line_str), end='')	# 可替换为sys.stdout.write()


# 替代方案
# 利用文件对象的行迭代器
# def filter_stream(function):
# 	for line_str in sys.stdin:
# 		print(function(line_str), end='')


if __name__ == '__main__':
	# 将stdin复制到stdout
	filter_stream(lambda line_str: line_str)
