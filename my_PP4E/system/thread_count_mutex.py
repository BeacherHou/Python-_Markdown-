#!/usr/bin/env python
"五个数数的线程，并同步化对stdout的访问"

import _thread
import time

MUTEX = _thread.allocate_lock()  # 创建全局锁对象


def counter(id_int, count_int):
	"从0数到count_int"
	for i_int in range(count_int + 1):
		MUTEX.acquire()  # 获取全局锁
		print('[{}] -> {}'.format(id_int, i_int))
		MUTEX.release()  # 释放全局锁
		time.sleep(1)


def main():
	for i_id_int in range(5):
		_thread.start_new_thread(counter, (i_id_int, 5))
	time.sleep(7)
	print('Main thread exiting ...')


if __name__ == '__main__':
	main()
