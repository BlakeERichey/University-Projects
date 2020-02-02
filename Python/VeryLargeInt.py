class Node:
  def __init__(self,data=None):
    self.data=data
    self.next=None
    self.prev=None

class VeryLargeInt:
  def __init__(self, number=None):
    self.head = None
    self.tail = None
    
    if number:
      for val in str(number):
        self.add(val)
  
  def add_node(self, node):
    if not self.head:
      self.head = node
      self.tail = node
    elif self.head and self.tail == self.head:
      self.tail = node
      self.head.next = self.tail
      self.tail.prev = self.head
    else:
      temp = self.tail
      self.tail = node
      temp.next = self.tail
      self.tail.prev = temp
  
  def add(self,data):
    node = Node(data)
    # print('adding', node.__dict__)
    self.add_node(node)

  def add_to_head(self, data):
    node = Node(data)

    if self.head:
      node.next = self.head
      self.head.prev = node
      self.head = node
    else:
      self.add_node(node)
  
  def remove_node(self, node):
    if node is self.head:
      self.head = self.head.next
      self.head.prev = None
    elif node.next and node.prev:
      node.prev.next, node.next.prev = node.next, node.prev
    elif node.prev and not node.next:
      node.prev.next = None
    elif not node.prev:
      self.head = None
      self.tail = None
  
  def remove(self, index):
    node = self.head
    i = 0
    while i < index and node is not None:
      node = node.next
      i+=1
    
    if i == index:
      self.remove_node(node)
    
  
  def __str__(self):
    s = ''
    node = self.head
    while node is not None:
      s += str(node.data)
      node = node.next
    return s
  
  def multiply(self, ll):
    node1 = self.tail
    node2 = ll.tail
    answer = None
    
    zeros = 0
    while node2:
      carry = 0
      current = node1 #number in list1 being multipled
      temp_list = VeryLargeInt()
      for i in range(zeros):
        temp_list.add(0)
      
      #multiply
      while current:
        digit1 = current.data
        digit2 = node2.data

        product = int(digit1)*int(digit2) + carry

        remainder, carry = product%10, product//10
        temp_list.add_to_head(remainder)

        current = current.prev
      
      if carry:
        temp_list.add_to_head(carry)

      #add zeros, move left in multiplier
      zeros += 1
      node2 = node2.prev

      # print(temp_list)
      #minimize answers space
      if answer is None:
        answer = temp_list
      else:
        answer.plus(temp_list)
    
    self.head = answer.head
    self.tail = answer.tail
  
  def plus(self, ll):
    '''
      takes 2 large ints and adds them together
    '''
    node1 = self.tail
    node2 = ll.tail

    carry = 0
    while node2 and node1:
      digit1 = node1.data
      digit2 = node2.data

      sum_ = int(digit1)+int(digit2) + carry
      node1.data, carry = sum_%10, sum_//10
      
      node1 = node1.prev
      node2 = node2.prev
    
    
    if node1 or node2:
      #if self is a longer number than ll
      while node1:  
        digit1 = node1.data

        sum_ = int(digit1) + carry
        node1.data, carry = sum_%10, sum_//10

        node1 = node1.prev
      
      #if ll is longer than self
      while node2:
        digit2 = node2.data
        
        sum_ = int(digit2) + carry
        digit1, carry = sum_%10, sum_//10

        self.add_to_head(digit1)
        node2 = node2.prev
    
    #add last carry to front of number
    if carry:
      self.add_to_head(carry)
  
  def factorial(num):
    vli = VeryLargeInt(1)

    for i in range(num):
      if i % 50 == 0:
        print(i)
      temp = VeryLargeInt(i+1)
      vli.multiply(temp)
    
    return vli
  

    

l = VeryLargeInt.factorial(1000)
print(l)