#!/usr/bin/env python


"将函数运行的结果重定向"


import sys


class Output:
	"类似文件的类，提供了write等方法"

	def __init__(self):
		self.text = ''

	def write(self, text_str):
		self.text += text_str

	def writelines(self, lines):
		for line_str in lines:
			self.write(line_str)


class Input:
	"类似文件的类，提供了read等方法"

	def __init__(self, input_str=''):
		self.text = input_str

	def read(self, size=None):
		if not size:
			r_text, self.text = self.text, ''
		else:
			r_text, self.text = self.text[:size], self.text[size:]

		return r_text

	def readline(self):
		n = self.text.find('\n')

		if n == -1:
			r_text, self.text = self.text, ''
		else:
			r_text, self.text = self.text[:n + 1], self.text[n + 1:]

		return r_text


def redirect(function, pargs_tuple, kargs_dict, input_str):
	"将函数运行的结果重定向"

	save_streams = sys.stdin, sys.stdout

	sys.stdin = Input(input_str=input_str)
	sys.stdout = Output()

	try:
		r_result = function(*pargs_tuple, **kargs_dict)
		r_output_str = sys.stdout.text
	finally:
		sys.stdin, sys.stdout = save_streams

	return r_result, r_output_str
