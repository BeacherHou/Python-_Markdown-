#!/usr/bin/python


def file_scanner(fn_str, function):
	"通用文件扫描例行函数"

	file = open(fn_str, 'r')

	while True:
		line_str = file.readline()
		if not line_str:
			break
		function(line_str)

	file.close()
