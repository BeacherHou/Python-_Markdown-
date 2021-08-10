#!/usr/bin/env python
"测试os._exit"

import os


def out_here():
	print('Bye os world')
	os._exit(11)
	print('Never reach')


if __name__ == '__main__':
	out_here()
