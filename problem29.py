import itertools
import sets

values = range(2, 101, 1)
answer = sets.Set([])

for perms in itertools.permutations(values, 2):
	answer.add(perms[0]**perms[1])

for i in values:
	answer.add(i ** i)	

print len(answer)