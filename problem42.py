def triangle_numbers(n):
	t = 0
	count = 0
	while t < n:
		count += 1
		t += count 
		yield t
		


words_file = open('problem42.txt', 'r')

words_list = words_file.read()

words_list = words_list.rsplit(',')

words_list = [currword.strip('"') for currword in words_list]

word_scores = []

for currword in words_list:
	word_scores.append(sum([ord(currlett)-64 for currlett in currword]))
			
triangle_numbers = list(triangle_numbers(max(word_scores)))

count = 0

print word_scores
print triangle_numbers

for i in word_scores:
	for j in triangle_numbers:
		if i == j:
			count += 1

print count