#!/usr/bin/env python
"使用threading模块做一个线程计数器"

import threading


class CountThread(threading.Thread):  # 继承子类Thread
	"线程计数器"

	def __init__(self, id_int, count_int, mutex):
		self.id_int = id_int
		self.count_int = count_int
		self.mutex = mutex
		threading.Thread.__init__(self)

	def run(self):  # run方法提供线程逻辑业务
		for i_count_int in range(self.count_int + 1):
			with self.mutex:
				print('[{}] -> {}'.format(self.id_int, i_count_int))


def main():
	mutex = threading.Lock()  # 与_thread.allocate_lock()相同
	threads_listCountThread = []

	for i_id_int in range(10):
		thread_CountThread = CountThread(i_id_int, 100, mutex)
		thread_CountThread.start()  # 在线程中开始运行run方法
		threads_listCountThread.append(thread_CountThread)

	for i_thread_CountThread in threads_listCountThread:
		i_thread_CountThread.join()  # 等待线程退出

	print('Main thread exiting...')


if __name__ == '__main__':
	main()
