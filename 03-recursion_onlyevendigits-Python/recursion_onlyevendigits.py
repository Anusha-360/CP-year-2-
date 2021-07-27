# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def readList():
    a = []
    for i in range(l):
        a.append(int(input()))
    return a
def convertEven(num, sum = 0):
    if num == 0:
        return sum
    else:
        if (num%10)%2 == 0:
            return convertEven(num//10, sum = sum*10+num%10)
        else:
            return convertEven(num//10, sum)
def prepareList(L, pos):
    if len(L) == pos:
        return L
    else:
        val = L[pos]
        L[pos] = reverseNum(convertEven(val))
        return prepareList(L, pos+1)
# num = (convertEven(num))
def reverseNum(num, sum = 0):
    if num == 0:
        return sum
    else:
        return reverseNum(num//10, sum = sum*10+num%10)
def fun_recursion_onlyevendigits(l):
    # your code goes here
    if len(l) == 0:
        return l
    return prepareList(l, 0)