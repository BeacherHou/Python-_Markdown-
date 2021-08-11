#!/usr/bin/env python
"""
派生一个子进程/程序，连接到我的stdin/stdout和子进程的stdin/stdout，
我的读写映射到派生程序的输出和输入上；很像利用subprocess模块绑定流一样
"""

import os
import sys


def spawn(prog_str, *args_tuple):  # 传入程序名称，命令行参数
	
	# 获取流的描述符
	stdin_fd_int = sys.stdin.fileno()
	stdout_fd_int = sys.stdout.fileno()

	# 创建两个IPC管道，用于双向通信
	parent_in_fd_int, child_out_fd_int = os.pipe()
	child_in_fd_int, parent_out_fd_int = os.pipe()

	pid_int = os.fork()
	if pid_int:
		"父进程"

		# 在父进程中关闭子进程端
		os.close(child_in_fd_int)
		os.close(child_out_fd_int)

		# 复制流
		os.dup2(parent_in_fd_int, stdin_fd_int)
		os.dup2(parent_out_fd_int, stdout_fd_int)
	else:
		"子进程"

		# 在子进程中关闭父进程端
		os.close(parent_in_fd_int)
		os.close(parent_out_fd_int)

		# 将管道的输入和输出流
		os.dup2(child_in_fd_int, stdin_fd_int)
		os.dup2(child_out_fd_int, stdout_fd_int)

		args_tuple = (prog_str,) + args_tuple
		os.execvp(prog_str, args_tuple)  # 复制到子进程的程序
		assert False, "Execvp failed!"  # 如果execvp调用失败，则会中断子进程


def main():
	my_pid_int = os.getpid()
	spawn('python', 'pipes_test_child.py', 'spam')  # 分支子程序

	print('Hello 1 from parent', my_pid_int)  # 发送到子进程的stdin
	sys.stdout.flush()  # 清理stdout缓冲区
	reply_str = input()  # 发自子进程的stdout
	sys.stderr.write('Parent got: "{}"\n'.format(reply_str))

	print('Hello 2 from parent', my_pid_int)
	sys.stdout.flush()
	reply_str = sys.stdin.readline()
	sys.stderr.write('Parent got: "{}"\n'.format(reply_str[:-1]))


if __name__ == '__main__':
	main()
