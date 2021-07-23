import sys


sum_int = 0
while True:
	line_str = sys.stdin.readline()
	if not line_str: break
	sum_int += int(line_str)
print(sum_int)
