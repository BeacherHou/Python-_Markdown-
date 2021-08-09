#!/usr/bin/env python
"编写线程的4种方法"

import threading
import _thread as thread
import time


def power(in_int, stdout_mutex):
	stdout_mutex.acquire()
	print('func |', in_int ** 32)
	stdout_mutex.release()


class PowerThread(threading.Thread):
	"带有状态的子类"

	def __init__(self, in_int, stdout_mutex):
		self.in_int = in_int
		self.stdout_mutex = stdout_mutex
		threading.Thread.__init__(self)

	def run(self):    # 重新定义run方法的行为
		self.stdout_mutex.acquire()
		print('child class |', self.in_int ** 32)
		self.stdout_mutex.release()


def main():
	stdout_mutex = threading.Lock()
	listThread = []

	# 基本线程模块
	thread.start_new_thread(power, (2, stdout_mutex))    # 所有线程都适用的接口

	# 带有状态的子类
	my_PowerThread = PowerThread(2, stdout_mutex)
	listThread.append(my_PowerThread)
	my_PowerThread.start()    # start方法调用run

	# 传入行为
	my_1_Thread = threading.Thread(
		target=(lambda: power(2, stdout_mutex))    # run调用target
	)
	listThread.append(my_1_Thread)
	my_1_Thread.start()

	# 同上，但是没有lambda函数将状态封装起来
	my_2_Thread = threading.Thread(
		target=power, args=(2, stdout_mutex)    # 可调用对象及其参数
	)
	listThread.append(my_2_Thread)
	my_2_Thread.start()

	for i_Thread in listThread:
		i_Thread.join()

	print('Main thread exiting...')


if __name__ == "__main__":
	main()
