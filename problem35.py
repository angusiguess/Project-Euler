import sets

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

sum = 0

def rotate(n):
	"""Takes a number, rotates it one place to the right"""
	n = str(n)
	return int(n[-1] + n[:-1])



prime_table = [False for i in range(10000001)]
primes = []

for i in gen_primes():
	if i > 1000000:
		break
	else:
		prime_table[i] = True
		primes.append(i)
		
print prime_table[:20]

print prime_table[rotate(29)]

circular_primes = sets.Set([])

for curr_prime in primes:
	if curr_prime >= 10:
		curr = curr_prime
		circular = True
		for i in range(len(str(curr))):
			curr = rotate(curr)
			if prime_table[curr] == False:
				circular = False
		if circular == True:
			circular_primes.add(curr_prime)
	else:
		circular_primes.add(curr_prime)
	
print len(circular_primes)