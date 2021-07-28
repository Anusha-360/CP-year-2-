"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    array = input_array
    while len(input_array) >= 1:
        
	    list = len(input_array)
	    
	    if (list % 2) != 0:
	    	middle_element = input_array[int(list/2)]
	    else:
	    	middle_element = input_array[int(list/2)-1]
	    
	    if value == middle_element:
	    	return array.index(middle_element)
  
	    elif value < middle_element:
	    	input_array = input_array[:(input_array.index(middle_element))]
      
	    elif value > middle_element:
	       input_array = input_array[(input_array.index(middle_element)+1):]

    return -1
# k = binary_search([1,2,3,4,5], 4)
# print(k)