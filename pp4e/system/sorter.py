import sys


lines_list = sys.stdin.readlines()
lines_list.sort()
for line_str in lines_list: print(line_str, end='')
