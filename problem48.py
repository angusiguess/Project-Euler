def n_raise_n(l):
	n = 1
	while n <= l:
		yield n**n
		n += 1
		
series = list(n_raise_n(1000))
sum = reduce(lambda x,y: x+y, series)
print str(sum)[-10:]


