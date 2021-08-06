#!/usr/bin/env python
"派生出子线程，直到输入“q”"


import _thread


def child(tid_int):
	"子线程"
	print('Hello from child!', tid_int)


def parent():
	"父线程"
	tid_int = 0
	while True:
		_thread.start_new_thread(child, (tid_int,))
		if input() == 'q':
			break
		tid_int += 1


if __name__ == '__main__':
	parent()
