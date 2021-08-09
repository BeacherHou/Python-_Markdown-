#!/usr/bin/env python
"在windows 7下每次运行打印不同的结果"

import threading
import time

COUNT_INT = 0


def adder():
	"间隔地给COUNT_INT加1"
	global COUNT_INT
	COUNT_INT += 1
	time.sleep(0.5)
	COUNT_INT += 1


def main():
	global COUNT_INT
	listThread = []

	for i_int in range(100):
		Thread = threading.Thread(target=adder)
		listThread.append(Thread)
		Thread.start()

	for i_Thread in listThread:
		i_Thread.join()

	print(COUNT_INT)


if __name__ == "__main__":
	main()
