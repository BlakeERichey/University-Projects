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