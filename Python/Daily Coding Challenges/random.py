# def packing(*l):
#   print(l)

# def unpacking(x, y, z):
#   print(x, y, z)

# def keywords(a, b, x, y):
#   print(a, b, x, y)

# packing('a', 'b', 'c')
# L = [4,5,6]
# unpacking(*L)

# #keyword arguements
# d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
# keywords(**d)

# def passfunc(demo):
#   demo('passed into passfunc')

# def demo(msg):
#   print(msg)

# passfunc(demo)


# import time
# L = [ [ 9, 10, 11, 12], [ 1,  2,  7, 13], [ 6, 16,  4, 14], [ 3,  8,  5, 15] ]
# import numpy as n;L=l=n.array(L);r,c=[0,3,0,3],136
# f=lambda r:L[r[0]:r[1],r[2]:r[3]]
# while n.any(l):y,x=map(int,n.where(L==n.amax(l)));r=[y-1,y+2,x-1,x+2];r=[max(x,0) for x in r];c-=L[y,x];L[y,x]=0;l=f(r)
# print(c)


# count = 0
# s=list(np.hstack(L)).index(16);s=(s%4,int(s/4))
# s=(s%4,int(s/4))  #current index
# def countCheese(arr):
#   currentIndex = (0,0)
#   for r, row in enumerate(arr):
#     for i, val in enumerate(row):
#       if val == 16:
#         currentIndex = (i, r)
#   print(currentIndex)
#   left = ( currentIndex[0]-1 , currentIndex[1] )
#   right = (currentIndex[0] + 1,currentIndex[1])
#   down = (currentIndex[0],currentIndex[1]+1)
#   up = (currentIndex[0],currentIndex[1] - 1)
#   print("left", left)
#   print('right', right)
#   print('down', down)
#   print('up', up)

# countCheese(L)



# import random, statistics

# def roll():
#   return random.choice(range(1,7))

# def getAttribute():
#   rolls = []
#   for i in range(0,4):
#     rolls.append(roll())
#   rolls.remove(min(rolls))
#   return rolls

# def getCharacterStats():
#   stats = []
#   for i in range(0, 6):
#     stats.append(sum(getAttribute()))
#   return stats

# count = 1
# stats = getCharacterStats()
# while statistics.mean(stats)<13:
#   count+=1
#   stats = getCharacterStats()
# print(stats, "AVG:", statistics.mean(stats), "Rolls", count)

#dex con wis str

# s=''.join([chr(x+97) for x in range(26)])
# print(s)

# stilts => stlilts   //1
# google => elgoogle  //2
# hannah => hannah    //0
# club   => bulclub   //3
# parras => sparraps  //2

# x,y=3,4
# print((0, 8)[6>y>=x>2])

# print(8>>x)

# arr2 = [2,2,3,2,3,5,3]   #5
# arr  = [6,1,6,6,13,13,13] #1

# def findSingle(L):
#   for val in L:
#     if L.count(val) != 3:
#       return val

# print(findSingle(arr2))

# class Greeting:

#   def __init__(self, msg):
#     self.msg=msg

#   def __str__(self):
#     return ''.join(map(chr, map(int, self.msg.split(','))))

# L = '87,101,108,99,111,109,101,33,32,72,111,112,101,32,121,97,108,108,32,108,105,107,101,32,105,116,32,104,101,114,101,33'
# print(Greeting(L))

# print(*L.split(','))


# s = "A paralegal is a person trained in legal matters who performs tasks requiring knowledge of the law and legal procedures. A paralegal is not a lawyer but can be employed by a law office or work freelance at a company or law office. Paralegals are not allowed to offer legal services directly to the public on their own and must perform their legal work under an attorney or law firm."
# import re
# rx=re.compile('[^a-zA-Z]');s=s.split(' ');D={}
# for i, val in enumerate(s):
#  s[i]=rx.sub('', val).lower()
# for val in s:
#  if val not in D.keys():
#   D[str(val)]=s.count(val)
# D=sorted(D.items(),key=lambda v:v[1],reverse=True)
# for t in D:
#   print(str(t[1]) + ":", t[0])

#Out: 'abdE'

from itertools import chain, combinations
def powersets(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    D = {}
    xs = list(iterable)
    # note we return an iterator rather than a list
    temp = list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))
   
    for i,x in enumerate(temp):
      D[i]=x
    return D

def findSubset(S, k):
  D=powersets(S)
  for key in D.keys():
    if(sum(D[key]) == k):
      return [x for x in D[key]]
  return None

S = [1,2,3,4,5]
k=42
print(findSubset(S, k))
