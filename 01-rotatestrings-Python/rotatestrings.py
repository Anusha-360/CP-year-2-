# Write the function rotatestring(s, n) that takes a string s and a possibly-negative integer n. 
# If n is non-negative, the function returns the string s rotated n places to the left. 
# If n is negative, the function returns the string s rotated |n| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
    n=n%len(s)
    rotate = s[n:] + s[:n]
    return rotate

