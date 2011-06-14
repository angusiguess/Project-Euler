def spiral_numbers(width):
	"""This is a generator for the numbers on the diagonal of a spiral.
	Specifically a set of 4 numbers is defined by adding a fixed gap
	four times to the last element of the set."""
	last_num = 0
	n = 0
	if n == 0:
		last_num = 1
		yield last_num
		n += 2
	while n < width:
		for i in range(4):
			last_num += n
			yield last_num
		n += 2

	
	

l = spiral_numbers(1001)	
print sum(l)
	