#!/usr/bin/env python
"用匿名管道从子进程向父进程发送数据，并将管道描述符封装进文件对象"

import os
import time


def child(pipe_out_int):
	"子进程"
	sleep_int = 0
	while True:
		# time.sleep(0.01)  # 防止向管道输出端发送的数据流重叠
		time.sleep(sleep_int)  # 模拟实际工作，让父进程等待
		msg_bytes = ('Spam {}\n'.format(sleep_int)).encode()  # 管道是二进制字节
		os.write(pipe_out_int, msg_bytes)  # 发送到父进程
		sleep_int += 1
		sleep_int %= 5  # 0到4，4到0


def main():
	pipe_in_int, pipe_out_int = os.pipe()  # 创建两个末端的管道

	if os.fork() == 0:  # 复制此进程
		os.close(pipe_in_int)  # 在此关闭输入端
		child(pipe_out_int)  # 在副本中运行child()
	else:
		os.close(pipe_out_int)  # 在此关闭输出端
		pipe_in_fdfile = os.fdopen(pipe_in_int)  # 创建文本模式输入文件对象
		while True:
			msg_bytes = pipe_in_fdfile.readline()[:-1]  # 数据发送之前保持阻塞
			print('Parent {} got [{}] at {}'.format(
				os.getpid(), msg_bytes, time.time()
			))


if __name__ == '__main__':
	main()
