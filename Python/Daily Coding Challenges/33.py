"""Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element."""
class RunningMedian():
  def __init__(self):
    self.vals=[]
    self.size=0
  
  def add(self,newVal):
    self.vals.append(newVal)
    self.vals=sorted(self.vals)
    self.size+=1
    length=self.size
    if length%2:
      print((self.vals[int(length/2)]))
    else:
      index=int(length/2)
      print((self.vals[index]+self.vals[index-1])/2)
L=[1,3,10,10]
start=RunningMedian()
for x in L:
  start.add(x)
