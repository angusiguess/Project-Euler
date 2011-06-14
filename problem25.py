def fibonacci_sequence():
	fib = 1
	prev_fib = 0
	n = 1
	while True:
		if n == 1:
			n += 1
			yield 1
		else:
			curr_fib = fib
			fib = fib + prev_fib
			prev_fib = curr_fib
			n += 1
			yield fib


n = 0
for i in fibonacci_sequence():
	n += 1
	if len(str(i)) == 1000:
		print n
		break