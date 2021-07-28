# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is l powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def getPrimeFactors(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
    
    return prime_factors

def isPowerfulNo(n):
    # get prime factors
    prime_factors = getPrimeFactors(n)
    
    # filter to get unique prime factors
    unique_prime_factors = set(prime_factors)
    for p in unique_prime_factors:
        if n % p != 0 or n % (p*p) != 0:
            return False
    return True

def nthpowerfulnumber(n):
	x=0
	y=0
	while(x<=abs(n)):
		y+=1
		if(isPowerfulNo(y)):
			x+=1
	return y