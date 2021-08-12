#!/usr/bin/env python
"测试信号"

import sys
import signal
import time


def now():
	"返回当前时间字符串"
	return time.ctime(time.time())


def on_signal(sign_num_int, stack_frame):
	"信号[sign_num_int]的信号事件处理器"
	# print(stack_frame)
	print(
		'Got signal {} at {}'.format(sign_num_int, now())
	)  # 多数信号事件处理器一直有效


def main():
	sign_num_int = sys.argv[1]
	signal.signal(sign_num_int, on_signal)  # 布置信号处理器

	while True:
		"等待信号"
		signal.pause()  # 或pass


if __name__ == '__main__':
	main()
