import math

def count_permutations(n, c):
	perms = math.factorial(n) / math.factorial(n - c)
	return perms


def count_combinations(n, c):
	combs = math.factorial(n) / (math.factorial(c) * math.factorial(n - c))
	return combs

print str(count_combinations(40, 20))