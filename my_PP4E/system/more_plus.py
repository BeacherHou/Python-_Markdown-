#!/usr/bin/env python
"""
分隔字符串或文本文件并交互的进行分页
"""


def get_reply():
	"读取用户交互式的回复键，即使stdin重定向到某个文件或者管道"
	import sys


	if sys.stdin.isatty():
		return input('More? ')
	else:
		if sys.platform[:3] == 'win':
			import msvcrt


			msvcrt.putch(b'More? ')
			key = msvcrt.getche()
			msvcrt.putch(b'\n')
			return key
		else:
			assert False, 'platform not supported'


def more(text_str, num_lines=15):
	lines = text_str.splitlines()
	while lines:
		chunk = lines[: num_lines]
		lines = lines[num_lines: ]
		for line in chunk: print(line)
		if lines and get_reply() not in [b'y', b'Y']: break


if __name__ == '__main__':
	import sys


	if len(sys.argv) == 1: more(sys.stdin.read())
	else: more(open(sys.argv[1]).read())
