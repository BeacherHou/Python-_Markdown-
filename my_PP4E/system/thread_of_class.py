#!/usr/bin/env python
"基于类的线程"

import threading
import _thread as thread
import time


class Power:
	"带有状态的非线程类，OOP方式"

	def __init__(self, in_int, stdout_mutex):
		self.in_int = in_int
		self.stdout_mutex = stdout_mutex

	def act(self):
		self.stdout_mutex.acquire()
		print('Power |', self.in_int ** 32)
		self.stdout_mutex.release()


def act(in_int, stdout_mutex):
	"利用嵌套作用域保留状态"
	def power():
		stdout_mutex.acquire()
		print('act |', 'power |', in_int ** 32)
		stdout_mutex.release()
	return power


def main():
	stdout_mutex = threading.Lock()

	obj_Power = Power(2, stdout_mutex)
	my_1_Thread = threading.Thread(target=obj_Power.act)  # 线程运行绑定方法
	my_1_Thread.start()

	my_2_Thread = threading.Thread(target=act(2, stdout_mutex))  # 线程运行返回的函数
	my_2_Thread.start()

	# 用基本的线程模块实现二者
	thread.start_new_thread(obj_Power.act, ())  # 线程运行一个可调用对象
	thread.start_new_thread(act(2, stdout_mutex), ())

	time.sleep(0.1)
	print('main | Main thread exiting...')


if __name__ == '__main__':
	main()
