sum_of_palindromes = 0
for i in range(1, 1000001, 1):
	#If the number is palindromic in base 2 and base 10, add to sum
	string_i = str(i)
	bin_string_i = str(bin(i))[2:] #Cut off the 0b
	if string_i == string_i[::-1] and bin_string_i == bin_string_i[::-1]:
		sum_of_palindromes += i
		
print sum_of_palindromes
	