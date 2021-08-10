#!/usr/bin/env python
"分支子进程，用os.wait观察其退出状态"

import os

EXIT_STAT_INT = 0


def child():
	"子进程"
	global EXIT_STAT_INT
	EXIT_STAT_INT += 1
	print('Hello from child', os.getpid(), EXIT_STAT_INT)
	os._exit(EXIT_STAT_INT)


def main():
	"父进程"
	while True:
		new_pid_int = os.fork()

		if new_pid_int == 0:
			child()
		else:
			pid_int, status_int = os.wait()
			print('Parent got', pid_int, status_int, status_int >> 8)
			if input() == 'q':
				break


if __name__ == '__main__':
	main()
