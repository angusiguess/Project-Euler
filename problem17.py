words_occurrences = [
	('onethousand', 1, 1000),
	('ninehundred', 100, 900),
	('eighthundred', 100, 800),
	('sevenhundred', 100, 700),
	('sixhundred', 100, 600),
	('fivehundred', 100, 500),
	('fourhundred', 100, 400),
	('threehundred', 100, 300),
	('twohundred', 100, 200),
	('onehundred', 100, 100),	
	('ninety', 90,90),
	('eighty', 90, 80),
	('seventy', 90,70),
	('sixty', 90, 60),
	('fifty', 90, 50),
	('forty', 90, 40),
	('thirty', 90, 30),
	('twenty', 90, 20),
	('nineteen', 10, 19),
	('eighteen', 10, 18),
	('seventeen', 10, 17),
	('sixteen', 10, 16),
	('fifteen', 10, 15),
	('fourteen', 10, 14),
	('thirteen', 10, 13),
	('twelve', 10, 12),	
	('eleven', 10, 11),
	('ten', 10, 10),
	('nine', 90, 9),
	('eight', 90, 8),
	('seven', 90, 7),
	('six', 90, 6),
	('five', 90, 5),
	('four', 90, 4),
	('three', 90, 3),
	('two', 90, 2),
	('one', 90, 1)
	#('and', 99*9, 'and'),
]

total_letters = 0
for i in range(1, 1001, 1):
	numberword = ''
	current_number = i
	while current_number > 0:
		for j in words_occurrences:
			if current_number >= j[2]:
				numberword += j[0]
				current_number -= j[2]
	print numberword
	total_letters += len(numberword)
	
print total_letters + (99*9*3)

#letter_sum = 0

#for current_occurrence in words_occurrences:
#	print len(current_occurrence[0]) * current_occurrence[1]
#	letter_sum += (len(current_occurrence[0])*current_occurrence[1])
	
#print letter_sum