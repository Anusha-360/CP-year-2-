# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...


def CheckLatinSquare(lst):
     
    # Your code goes here...
    # Size of square matrix is NxN
    N = len(lst)
  
    # Vector of N sets corresponding
    # to each row.
    rows = []
    for i in range(N):
        rows.append(set([]))
  
    # Vector of N sets corresponding
    # to each column.
    cols = []
    for i in range(N):
        cols.append(set([]))
  
    # Number of invalid elements
    invalid = 0
  
    for i in range(N):
        for j in range(N):
            rows[i].add(lst[i][j])
            cols[j].add(lst[i][j])
  
            if (lst[i][j] > N or lst[i][j] <= 0) :
                invalid += 1
             
    # Number of rows with
    # repetitive elements.
    numrows = 0
  
    # Number of columns with
    # repetitive elements.
    numcols = 0
  
    # Checking size of every row
    # and column
    for i in range(N):
        if (len(rows[i]) != N) :
            numrows+=1
         
        if (len(cols[i]) != N) :
            numcols+=1
  
    if (numcols == 0 or numrows == 0 and invalid == 0) :
        return True
    else:
        return False
 
Matrix = CheckLatinSquare([  [ 1, 2, 3, 4 ],
             [ 2, 1, 4, 3 ],
             [ 3, 4, 1, 2 ],
             [ 4, 3, 2, 1 ] ])
  
# Function call
print(Matrix)
