#!/usr/bin/env python
"五个数数的线程"

import _thread
import time


def counter(id_int, count_int):
	"从0数到count_int"
	for i_int in range(count_int + 1):
		print('[{}] -> {}'.format(id_int, i_int))
		time.sleep(1)


def main():
	for i_int in range(5):
		_thread.start_new_thread(counter, (i_int,5))
	time.sleep(7)


if __name__ == '__main__':
	main()
