#!/usr/bin/env python
"测试套接字（独立启动程序）"

from socket_preview import server, client  # 二者使用相同的端口号
import sys
import os
from threading import Thread


def main():
	mode = sys.argv[1]

	if mode == 'server':  # 在这个进程中运行服务器
		server()
	elif mode == 'client':  # 在这个进程中运行客户端
		client('Client: process={}'.format(os.getpid()))
	else:  # 在这个进程中运行5个客户端线程
		for i_id_int in range(5):
			Thread(
				target=client, 
				args=('Client: process={} thread={}'.format(os.getpid(), i_id_int),)
			).start()


if __name__ == '__main__':
	main()
