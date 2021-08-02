sum_int = 0

while True:
	try: data_str = input()
	except EOFError: break
	else:
		sum_int += int(data_str)

print(sum_int)
