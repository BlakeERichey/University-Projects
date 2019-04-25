#import BTNode, Tree
import random
from BTree  import BTree 
from BTNode import BTNode

def main():
  BT = BTree(BTNode(125))
  for i in range(0, 100):
    BT.insert(random.randint(0,500))

  BT.inorder()
  while True:
    print(BT.contains(int(input('Whats your Query? '))))

main()