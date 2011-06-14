from math import sqrt, ceil
import time

list_primes = []

def triangle_numbers():
	t = 0
	count = 0
	while True:
		count += 1
		t += count 
		yield t		


def factors(n):
	num_factors = 0
	for i in range(1, n + 1, 1):
		if n % i == 0:
			num_factors += 1
	return num_factors

	
def gen_primes():
	"""Sieve of Eratosthenes"""
	D = {}
	q = 2
	
	while True:
		if q not in D:
			yield q
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

def count_factors(n):
	'''Another possible solution, use prime factorization to count the number of factors more
	efficiently. Every number can be represented as a product of primes, so we go through every
	prime from 2 to sqrt(n), divide by all divisible primes. This gives us a number in the format
	p^x*q^y*r^z. If we multiply (x+1)(y+1)(z+1) we will get the result.'''
	factors = []
	for p in list_primes:
		count = 0
		while n % p == 0:
			n = n / p
			count += 1
		if count > 0:
			factors.append(count)
	
	if len(factors) == 0:
		return 2
	
	factors = map(lambda x: x + 1, factors)
	num_factors = reduce(lambda x,y: x * y, factors)
	return num_factors
	
	
last_prime = 1
p = gen_primes()

x = time.time()
for i in triangle_numbers():
	while last_prime < sqrt(i):
		last_prime = p.next()
		list_primes.append(last_prime)
	if count_factors(i) > 500:
		print i
		break
print "Solved in " + str(time.time() - x) + " seconds."
		
#print list_primes
#x = time.time()
#for i in triangle_numbers():
#	if factors(i) > 500:
#		print i
#		break
#print "Solved in " + str(time.time() - x) + " seconds."
