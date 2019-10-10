##Blake Richey

#Used to create a binary tree that is sorted
#when a value is added to the binary tree that already exists in the tree,
#that value is always added to the right of the corresponding node
class BTNode():

  def __init__(self, val):
    self.data  = val
    self.left  = None
    self.right = None
  
  def getData(self):
    return self.data

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def setLeft(self, newVal):
    self.left = BTNode(newVal)

  def setRight(self, newVal):
    self.right = BTNode(newVal)

  def isLeaf(self):
    return self.left == None and self.right == None

class BTree():

  def __init__(self, rootNode):
    self.root = (None, rootNode)[rootNode != None]
  
  def getRoot(self):
    return self.root

  def setRoot(self, Node):
    self.root = Node

  #inserts a node that contains `val`
  def insert(self, val):
    if self.root == None:
      self.root=BTNode(val)
    else:
      currentNode = self.helperAddNode(self.root, val)
      if val > currentNode.getData():     #add to right of node
        currentNode.setRight(BTNode(val))
      elif val < currentNode.getData():   #add to left of node
        currentNode.setLeft(BTNode(val))
      elif val == currentNode.getData():  #node has same value
        tempNode = BTNode(val)
        if currentNode.getRight():
          tempNode.setRight(currentNode.getRight())
          currentNode.setRight(tempNode)
        else:
          currentNode.setRight(tempNode)

  #gets node to insert onto, returns node
  def helperAddNode(self, currentNode, val):
    if(currentNode.getData() > val):    #go left
      if(currentNode.isLeaf() or currentNode.getLeft() == None):
        return currentNode
      else:
        return self.helperAddNode(currentNode.getLeft(), val)
    elif(currentNode.getData() < val):  #go right
      if(currentNode.isLeaf() or currentNode.getRight() == None):
        return currentNode
      else:
          return self.helperAddNode(currentNode.getRight(), val)
    elif(currentNode.getData() == val): #adding existing value
      return currentNode

  #prints entire tree using inorder traversal
  def inorder(self):
    self.helperInorder(self.root)
    print('')

  #to get whole tree call using root as tempNode
  def helperInorder(self, tempNode):
    if not tempNode:
      return
    
    self.helperInorder(tempNode.getLeft())
    print(tempNode.getData(), end = ' ')
    self.helperInorder(tempNode.getRight())

  #returns true if val is contained in binary tree
  def contains(self, val):
    node = self.find(val)
    if node != None:
      return True
    return False
  
  #returns Node that contains val as its `data` field using entire tree
  def find(self, val):
    return self.helperFind(self.root, val)

  #returns node of tree that contains `val`
  def helperFind(self, currentNode, val):
    #---exit conditions---
    if currentNode == None:
      return None

    if currentNode.isLeaf():
      if currentNode.getData() == val:
        return currentNode
      else:
        return None

    #continue searching
    data = currentNode.getData()
    if data == val:
      return currentNode
    else:
      if data > val:
        return self.helperFind(currentNode.getLeft(), val)
      elif data < val:
        return self.helperFind(currentNode.getRight(), val)