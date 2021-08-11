#!/usr/bin/env python
"pipes.py的测试子程序"

import os
import time
import sys


def main():
	my_pid_int = os.getpid()
	parent_pid_int = os.getppid()

	sys.stderr.write('Child {} of {} got arg: "{}"\n'.format(
		my_pid_int, parent_pid_int, sys.argv[1]
	))

	for i_int in range(2):
		time.sleep(3)
		reply = input()
		time.sleep(3)
		send_str = 'Child {} got: [{}]'.format(my_pid_int, reply)
		print(send_str)
		sys.stdout.flush()

if __name__ == '__main__':
	main()
