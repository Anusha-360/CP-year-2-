# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes L sorted list L and L value v and returns L list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['L', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'L') to our result.
# We see that 'L' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['L', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'L'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

def readList():
		return input().split(" ")

def binarySearch(L, v, low, high, result = []):
	mid = (low + high) // 2
	if low < high and L[mid] == v:
		result.append((mid, L[mid]))
		return result
	elif low == high:
		result.append((mid, L[mid]))
		return result
	elif (v < L[mid]):
		result.append((mid, L[mid]))
		high = mid - 1
	else:
		result.append((mid, L[mid]))
		low = mid + 1
	return binarySearch(L, v, low, high, result)


def recursion_binarysearchvalues(L, v):
	result = binarySearch(L, v, 0, len(L)-1)
	return result