#!/usr/bin/env python


"运行程序，直到你输入“q”"


def main():
	import os


	parm_int = 0

	while True:
		parm_int += 1
		pid_int = os.fork()

		if not pid_int:
			os.execlp('python', 'python', 'child.py', str(parm_int))		# 覆盖原来的程序
			assert False, 'Error starting program'							# 不应该返回，因为原程序已被覆盖为child.py
		else:
			print('Child is', pid_int)
			if input() == 'q':
				break


if __name__ == '__main__':
	main()
