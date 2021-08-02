#!/usr/bin/env python


"以递归的方式列举目录树中的文件"


import os


def my_lister_walk(root_dir_str):
	print('[' + root_dir_str + ']')


	for file_str in os.listdir(root_dir_str):
		path_str = os.path.join(root_dir_str, file_str)

		if os.path.isdir(path_str):
			my_lister_walk(path_str)
		else:
			print(path_str)


if __name__ == '__main__':
	import sys


	sys.stdout = open('my_lister_walk.out', 'w')
	my_lister_walk('../../PP4E')
