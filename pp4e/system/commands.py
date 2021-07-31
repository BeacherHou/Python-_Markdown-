#!/usr/bin/python

from sys import argv
from scan_file import file_scanner


class UnknownCommand(Exception):
	"一个“未知命令”异常的类"

	pass


def process_file(line_str):
	"一个逐行将“*name”和“+name”转换为“Ms.name”和“Mr.name”的函数"

	if line_str[0] == '+':
		# 剥去开头和末尾的字符：\n
		print('Mr.' + line_str[1:-1])
	elif line_str[0] == '*':
		print('Ms.' + line_str[1:-1])
	else:
		# 抛出异常
		raise UnknownCommand(line_str)


if len(argv) == 2:
	# 允许通过文件名命令行参数传入文件
	fn_str = argv[1]
else:
	fn_str = 'data.txt'

# 运行扫描器
file_scanner(fn_str, process_file)
