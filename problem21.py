from math import sqrt

def amicable_mapping(n):
	l = []
	
	if n > 1:
		l.append(1)
	
	i = 2
	
	while i < n:
		if n % i == 0 and i not in l:
			l.append(i)
			if n / i not in l:
				l.append(n / i)
		i += 2
	l.sort()
	return sum(l)			
	
		
	

amicable_map = {}

for i in range(1, 10001, 1):
	mapping = amicable_mapping(i)
	if mapping > 1 and mapping <= 10000:
		amicable_map[i] = mapping
		
print amicable_map

amicable_sum = 0
amicable_nums = []

for (k,v) in amicable_map.items():
	if v in amicable_map:
		if k == amicable_map[v] and k != v:
				amicable_nums.append(k)
				amicable_nums.append(v)
				
amicable_nums = list(set(amicable_nums))
print amicable_nums


print sum(amicable_nums)