#!/usr/bin/env python
"利用mutex在父线程中探知子线程何时结束"

import _thread as thread

MUTEX = thread.allocate_lock()
NUMS_THREAD_INT = 10
LISTMUTEX = [thread.allocate_lock() for i_int in range(NUMS_THREAD_INT)]


def counter(id_int, count_int):
	"数数"
	for i_int in range(count_int + 1):
		MUTEX.acquire()
		print('[{}] -> {}'.format(id_int, i_int))
		MUTEX.release()
	LISTMUTEX[id_int].acquire()  # 向主线程发送信号


def main():
	for i_id_int in range(NUMS_THREAD_INT):
		thread.start_new_thread(counter, (i_id_int, 100))
	for i_mutex in LISTMUTEX:
		while not i_mutex.locked():
			pass
	print('Main thread exiting...')


if __name__ == '__main__':
	main()
