#!/usr/bin/env python
"派生子线程，查看其返回状态和共享状态"

import _thread as thread

EXIT_STAT_INT = 0


def child():
	"子线程"
	global EXIT_STAT_INT
	EXIT_STAT_INT += 1
	thread_id_int = thread.get_ident()
	print('Hello from child', thread_id_int, EXIT_STAT_INT)
	thread.exit()
	print('Never reach')


def main():
	while True:
		thread.start_new_thread(child, ())
		if input() == 'q':
			break


if __name__ == '__main__':
	main()
