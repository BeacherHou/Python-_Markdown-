#!/usr/bin/env python
"""
分隔字符串或文本文件并交互的进行分页
"""


def more(text_str, num_lines=15):
	lines = text_str.splitlines()
	while lines:
		chunk = lines[: num_lines]
		lines = lines[num_lines: ]
		for line in chunk: print(line)
		if lines and input('More?') != '': break


if __name__ == '__main__':
	import sys


	if len(sys.argv) == 1: more(sys.stdin.read())
	else: more(open(sys.argv[1]).read())
