alphabet_score = {}
n = 0
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
	n += 1
	alphabet_score[i] = n
	
f = open('p22names.txt', 'r')

l = f.read()

l = l.split(',')
l = [curr.replace('"', '') for curr in l]
l = sorted(l)

scores = []

for i in l:
	remap = map(lambda x: alphabet_score[x], i)
	score = reduce(lambda x,y: x+y, remap) * l.index(i)
	scores.append(score)


print sum(scores)

#print l
#n = 0
#for i in l:
#	n += 1
#	score = 0
#	for j in i:
#		score += alphabet_score[j]
#	scores.append(score * n)

#print sum(scores)

#print l
