class Node():
  def __init__(self, val):
    self.data = val if val != None else None
    self.next = None
    self.prev = None

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
      self.tail.next.prev=self.tail
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
  
  def clear(self):
    self.head=None
    self.tail=None
