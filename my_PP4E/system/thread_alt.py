#!/usr/bin/env python
"所有三个线程均打印“4294967296”"

import _thread
import time


def power(a_int):
	"打印a_int的32次方"
	print(a_int ** 32)


class Power:
	"次方"
	def __init__(self, a_int):
		self.a_int = a_int

	def act(self):
		"打印a_int的32次方"
		print(self.a_int ** 32)


def main():
	# 简单函数
	_thread.start_new_thread(power, (2,))
	# 待执行的lambda函数
	_thread.start_new_thread(lambda: power(2), ())
	# 绑定方法对象
	obj_Power = Power(2)
	_thread.start_new_thread(obj_Power.act, ())
	time.sleep(0.01)	# 防止主线程较早退出


if __name__ == '__main__':
	main()
