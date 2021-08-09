#!/usr/bin/env python
"每次都打印200，因为共享资源的访问已经同步化"

import threading
import time

COUNT_INT = 0


def adder(count_int_mutex):
	"间隔地给COUNT_INT加1"
	global COUNT_INT
	with count_int_mutex:
		COUNT_INT += 1
	time.sleep(0.5)
	with count_int_mutex:
		COUNT_INT += 1


def main():
	global COUNT_INT
	count_int_mutex = threading.Lock()
	listThread = []

	for i_int in range(100):
		Thread = threading.Thread(target=adder, args=(count_int_mutex,))
		listThread.append(Thread)
		Thread.start()

	for i_Thread in listThread:
		i_Thread.join()

	print(COUNT_INT)


if __name__ == "__main__":
	main()
