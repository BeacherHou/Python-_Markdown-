#!/usr/bin/env python
"命名管道的测试程序：运行命令无参数时用parent监听，有参数则用child写入管道"

import os
import time
import sys

FIFO_PATH_STR = '/tmp/pipefifo'


def child():
	"模拟客户端程序：向服务器数据发送数据"
	# print('Start child')
	pipe_out_int = os.open(FIFO_PATH_STR, os.O_WRONLY)
	sleep_int = 0

	while True:
		time.sleep(sleep_int)
		msg_bytes = 'Spam {}\n'.format(sleep_int).encode()
		os.write(pipe_out_int, msg_bytes)
		# print('Child write "{}"'.format(msg_bytes))
		sleep_int = (sleep_int + 1) % 5


def parent():
	"模拟服务器程序：监听管道"
	# print('Start parent')
	pipe_in_file = open(FIFO_PATH_STR, 'r')

	while True:
		# print('Hello')
		msg_str = pipe_in_file.readline()[:-1]  # 数据发送完之前保持阻塞
		print('Parent {} got "{}" at {}'.format(os.getpid(), msg_str, time.time()))


def main():
	if not os.path.exists(FIFO_PATH_STR):
		os.mkfifo(FIFO_PATH_STR)  # 创建一个命名管道文件

	# print(sys.argv)
	if len(sys.argv) == 1:
		parent()
	else:
		child()


if __name__ == '__main__':
	main()
