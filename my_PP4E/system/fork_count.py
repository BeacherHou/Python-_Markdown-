#!/usr/bin/env python


"""
分支进程基本操作：本程序启用了5个副本，与原有程序并行运行；每个副本在一个标准输入/输出流上重复5次。
"""


import os
import time


def counter(count_int):
	"子进程"

	for i_int in range(count_int + 1):
		time.sleep(0.25)
		print('\n{pid_int} -> {i_int}'.format(pid_int=os.getpid(), i_int=i_int))


if __name__ == '__main__':
	for i_int in range(5):
		pid_int = os.fork()

		if pid_int != 0:
			print('Process {pid_int} spawned'.format(pid_int=pid_int))
		else:
			counter(60)
			os._exit(0)

	print('Main process exiting.')
