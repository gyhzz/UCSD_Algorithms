def fib_num(n):

	fib_list = []

	fib_list.append(0)
	fib_list.append(1)

	if n == 0:
		return 0
	
	if n == 1:
		return 1

	for i in range(2, n + 1):
		fib_list.append(fib_list[i - 1] + fib_list[i - 2])

	return fib_list[n]


if __name__ == '__main__':
	
	n = int(input())
	print(fib_num(n))