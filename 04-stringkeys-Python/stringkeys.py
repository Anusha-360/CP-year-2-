"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
       self.table = ['']*10000
 
    def store(self, string):
       """Input a string that's stored in
       the table."""
       # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
       # Your code goes here
      
       a = self.calculate_hash_value(string)
       if(self.table[a]!= None):
           self.table[a] = (string)
       else:
           self.table[a] = [string]
       return a
      
    def lookup(self, string):
       """Return the hash value if the
       string is already in the table.
       Return -1 otherwise."""
       a = self.calculate_hash_value(string)
       if(string in self.table[a]):
           return a
       return -1
      
 
    def calculate_hash_value(self, string):
       """Helper function to calulate a
       hash value from a string."""
       hashvalue = ord(string[0])*100 + ord(string[1])
       return hashvalue
   
#reference: http://www.openbookproject.net/books/pythonds/SortSearch/Hashing.html