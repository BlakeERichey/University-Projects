class Node():
  def __init__(self, val):
    self.data = val if val != None else None
    self.next = None

class Queue():
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, val):
    if self.head == None:
      self.head = Node(val)
      self.tail = self.head
    else:
      self.tail.next = Node(val)
      self.tail = self.tail.next
  
  def dequeue(self):
    if self.head == None:
      return None
    else:
      rv = self.head
      self.head = self.head.next
      return rv.data
  
  def isEmpty(self):
    return self.head == None

  #view front of line
  def front(self):
    return self.head.data

  #view last in line
  def last(self):
    return self.tail.data
  
  def getList(self):
    if self.head == None:
      return None
    else:
      vals = []
      currentNode = self.head
      while currentNode != None:
        vals.append(currentNode.data)
        currentNode = currentNode.next
      return vals


L = Queue()
L.enqueue(5)
L.enqueue(4)
print(L.dequeue())
L.enqueue(3)
L.enqueue(9)
print('Last', L.last())
print(L.dequeue())
print(L.dequeue())
print(L.dequeue())
L.enqueue(6)
print('Front', L.front())
print(L.isEmpty())
print(L.getList())
