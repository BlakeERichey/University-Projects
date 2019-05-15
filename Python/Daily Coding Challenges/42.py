"""Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null."""
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
k=9
print(findSubset(S, k))
