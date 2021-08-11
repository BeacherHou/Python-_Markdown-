#!/usr/bin/env python
"匿名管道和线程而非进程，可在windows上工作"

import os
import time
import threading


def child(pipe_out_int):
	sleep_int = 0

	while True:
		time.sleep(0.01)
		time.sleep(sleep_int)
		msg_bytes = ('Spam {}'.format(sleep_int)).encode()
		os.write(pipe_out_int, msg_bytes)
		sleep_int += 1
		sleep_int %= 5


def parent(pipe_in_int):
	while True:
		msg_bytes = os.read(pipe_in_int, 32)
		print('Parent {} got [{}] at {}'.format(
			os.getpid(), msg_bytes, time.time()
		))


def main():
	pipe_in_int, pipe_out_int = os.pipe()
	threading.Thread(target=child, args=(pipe_out_int,)).start()
	parent(pipe_in_int)


if __name__ == '__main__':
	main()
