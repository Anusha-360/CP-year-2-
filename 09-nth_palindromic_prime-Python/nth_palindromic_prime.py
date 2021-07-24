# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

def isPalindrome(n):
	temp = n
	reverse_num = 0
	while(n>0):
		digit = n % 10
		reverse_num = reverse_num*10 + digit
		n = n // 10
	if(temp == reverse_num):
		return True
	else:
		return False

def isPalindromicPrime(n):
	if(isPrime(n) == True and isPalindrome(n) == True):
		return True
	else:
		return False

def fun_nth_palindromic_prime(n):
	test = 1
	count = 0
	while(count <= n):
		if(isPalindromicPrime(test) == True):
			palindromicPrime = test
			count += 1
		test += 1
	return palindromicPrime

# print(fun_nth_palindromic_prime(n):(int(input())))