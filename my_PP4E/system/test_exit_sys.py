#!/usr/bin/env python
"测试sys.exit"

import sys


def later():
	print('Bye sys world')
	sys.exit(11)
	print('Never reached')


if __name__ == '__main__':
	later()
