#!/usr/bin/env python


def get_option_name(sys_argv_list):
	"扫描sys_argv_list列表查找-option_name option_value值对，并保存到字典r_option_dict返回"
	r_option_dict = {}
	while sys_argv_list:
		if sys_argv_list[0][0] == '-':
			r_option_dict[sys_argv_list[0]] = sys_argv_list[1]
			del(sys_argv_list[:2])
		else:
			del(sys_argv_list[0])
	return r_option_dict


if __name__ == '__main__':
	import sys
	print(get_option_name(sys.argv))
