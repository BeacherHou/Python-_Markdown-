#!/usr/bin/env python
"thread_count_wait_2.py的替代方案"

import _thread as thread
import time

NUMS_THREAD_INT = 5
EXIT_LISTBOOL = [False for i_int in range(NUMS_THREAD_INT)]


def counter(id_int, count_int, mutex):
	"数数的子进程"
	for i_count_int in range(count_int + 1):
		time.sleep(0.1 / (id_int + 1))
		with mutex:
			print('[{}] -> {}'.format(id_int, i_count_int))
	EXIT_LISTBOOL[id_int] = True


def main():
	mutex = thread.allocate_lock()
	for i_id_int in range(NUMS_THREAD_INT):
		thread.start_new_thread(counter, (i_id_int, 5, mutex))
	while not all(EXIT_LISTBOOL):
		time.sleep(1)
	print('Main thread exiting...')


if __name__ == '__main__':
	main()
