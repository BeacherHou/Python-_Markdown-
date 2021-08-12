#!/usr/bin/env python
"测试signal.alarm"

import sys
import signal
import time


def on_signal(sign_num_int, stackframe):
	"信号处理器"
	print('Got alarm {} at {}'.format(sign_num_int, time.asctime()))


def main():
	while True:
		signal.signal(signal.SIGALRM, on_signal)
		print('Setting at', time.asctime())
		signal.alarm(5)  # 5秒后发送信号
		signal.pause()


if __name__ == '__main__':
	main()
