#!/usr/bin/env python


"用os.walk完成目录树列举"


import os


def lister_walk(root_dir_str):
	for cur_dir_str, sub_dir_list, file_list in os.walk(root_dir_str):
		print('[' + cur_dir_str + ']')
		for file_str in file_list:
			print(os.path.join(cur_dir_str, file_str))


if __name__ == '__main__':
	import sys


	sys.stdout = open('lister_walk.out', 'w+')
	lister_walk('../../PP4E')
