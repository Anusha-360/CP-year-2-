# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withproperty309(n):
    a = n **5
    b = str(a)
    c = '0123456789'
    for i in c:
        if(i in b):
            continue
        else:
            return False
    return True

def nthwithproperty309(n):
    # Your code goes here
    f = -1
    g = 0
    while(f < n):
        g = g + 1
        if(withproperty309(g)):
            f = f + 1
    return g