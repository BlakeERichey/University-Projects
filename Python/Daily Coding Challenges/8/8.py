#import BTNode, Tree

from BTree  import BTree 
from BTNode import BTNode

def main():
  BT = BTree(BTNode('d'))
  BT.insert('b')
  BT.insert('c')
  BT.insert('e')
  BT.insert('d')
  BT.insert('g')

  BT.inorder()
  print(BT.contains('c'))

main()