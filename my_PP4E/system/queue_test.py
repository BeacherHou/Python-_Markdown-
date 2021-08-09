#!/usr/bin/env python
"生产者和消费者线程与共享队列进行通信"

import threading
import time
import queue

NUM_CONSUMERS_INT = 2  # 消费者线程数目
NUM_PRODUCERS_INT = 4  # 生产者线程数目
NUM_MESSAGES_INT = 4  # 每个生产者存入的信息的数量
STDOUT_MUTEX = threading.Lock()  # 否则打印操作可能会发生重叠
DATA_QUEUE = queue.Queue()
EXIT_LISTBOOL = [False for i_int in range(NUM_PRODUCERS_INT)]  # 消费者线程退出的标志


def produser(id_int):
	"生产者线程"
	for i_message_num_int in range(NUM_MESSAGES_INT):
		time.sleep(id_int + 1)
		DATA_QUEUE.put(
			'[producer id={}, count={}]'.format(id_int, i_message_num_int)
		)
	EXIT_LISTBOOL[id_int] = True


def consumer(id_int):
	"消费者线程"
	while not all(EXIT_LISTBOOL):
		time.sleep(0.1314)

		try:
			data_str = DATA_QUEUE.get(block=False)
		except queue.Empty:
			pass
		else:
			with STDOUT_MUTEX:
				print('consumer', id_int, '| got ->', data_str)


def main():
	listThread = []

	for i_id_int in range(NUM_CONSUMERS_INT):
		Thread = threading.Thread(target=consumer, args=(i_id_int,))
		listThread.append(Thread)
		Thread.start()

	for i_id_int in range(NUM_PRODUCERS_INT):
		Thread = threading.Thread(target=produser, args=(i_id_int,))
		listThread.append(Thread)
		Thread.start()

	for i_Thread in listThread:
		i_Thread.join()

	print('Main thread exiting...')


if __name__ == '__main__':
	main()
