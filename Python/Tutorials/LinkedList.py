class Node():
  def __init__(self, val):
    self.data=(None, val)[val!=None]
    self.prev=None
    self.next=None
  
  def getData(self):
    return self.data
  
  def getPrev(self):
    return self.prev

  def getNext():
    return self.next
  
  def setData(self, val):
    self.data=val

  def setNext(self, node):
    self.next=node

  def setPrev(self, node):
    self.prev=node

class LinkedList():

  #constructor. Always starts with an empty list
  def __init__(self):
    pass

  #adds a new node containing `val` as its data componenet. appends to the end of the list
  def add(self, val):
    pass

  #removes the node passed in from the linked list if present
  def remove(self, node):
    pass

  #returns the first element of the linked list
  def getHead(self):
    pass

  #returns the last element of the linked list
  def getTail(self):
    pass

  #returns number of nodes in linked list
  def getLength(self):
    pass

  #attempts to return the sum of all elements in the list. if any element is not a numerical value it returns None (as the data type)
  def sum(self):
    pass  

##THE ABOVE CODE SHOULD BE IMPLEMENTED TO SOLVE THE FOLLOWING PROBLEM. CODE BELOW HERE SHOULD NOT BE CHANGED, BUT SHOULD BE TESTED TO CONFIRM ACCURACY

L=LinkedList()
L.add(5)  #5
L.add(3)  #5,3
temp=L.getHead() 
L.remove(temp) #3
print(L.getHead().getData()) #prints 3

L=LinkedList()
L.add(3)
L.add(4)
L.add(5)
print(L.sum()) #12
L.add('add this?')
print(L.sum()) #returns None

L=LinkedList()
L.add('how many')
L.add('questions')
L.add('can')
L.add('I')
L.add('Ask')
L.add('?')
curNode=L.getHead()
while curNode and curNode.getData() != None:
  print(curNode.getData(), end=' ') #should print 'how many questions can i ask?'
  curNode = curNode.getNext()
