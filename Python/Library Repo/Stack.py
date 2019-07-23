class Node():
  def __init__(self, val):
    self.data = val if val != None else None
    self.next = None

class Stack():
  def __init__(self, val):
    self.head = Node(val)
  
  def push(self, val):
    if self.head == None:
      self.head = Node(val)
    else:
      newNode = Node(val)
      newNode.next = self.head
      self.head = newNode

  def pop(self):
    if self.head == None:
      return
    rv = self.head
    self.head = self.head.next
    return rv.data

  def peek(self):
    if self.head == None:
      return None
    else:
      return self.head.data

  def isEmpty(self):
    return self.head == None

'''
#Test
newStack = Stack(2)
newStack.push(3)
newStack.push(4)
newStack.push(5)
newStack.push(7)
newStack.push(3)


#remove from stack based on time, fun experiment
import time as s
removeFromStack = True
time = 1
while removeFromStack == True:
  if time == 11:
    time = 1
  if(newStack.peek() == None):
    removeFromStack = False
  if(newStack.peek() == time):
    print(newStack.pop())
  s.sleep(.2)
  time += 1
'''