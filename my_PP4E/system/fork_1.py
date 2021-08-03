#!/usr/bin/env python

"分支出子进程，直到你输入“q”"


import os


def child():
	"子进程"

	print('Hello from child! pid ->', os.getpid())


def parent():
	"父进程"

	while True:
		new_pid_int = os.fork()

		if new_pid_int == 0:
			child()
			os._exit(0)	# 否则回到父循环中
		else:
			print('Hello from parent! parent_pid ->', os.getpid(),
				'child_pid ->', new_pid_int)

		if input() == 'q':
			break


if __name__ == '__main__':
	parent()
