# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
    dozens= int(eggs/12)
    if(eggs%12==0):
        return dozens
    else:
        return dozens+1
