"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None): 
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element) #adding new element at the tail of the queue

    def peek(self):
        return self.storage[0]  #returing the top element with out deleting it fron the queue
    def dequeue(self):
        return self.storage.pop(0)  #it delete the top element