# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def digitcount(i , n):
	count = 0
	while(n > 0):
		a = n % 10
		if(a == i):
			count = count + 1
		n = n //10
	return count
def mostfrequentdigit(n):
	digit = -1
	frequency = -1
	for i in range(0 , 10):
		count = digitcount(i , n)
		if(count > frequency):
			frequency = count
			digit = i			
	return digit


