import itertools

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

permutations = []

permute = itertools.permutations(digits, 10)

for i in range(1, 1000001, 1):
	answer = permute.next()
	print answer

answer = reduce(lambda x,y: x + y, answer)
print answer
