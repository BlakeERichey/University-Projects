"""Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null."""
from itertools import chain, combinations
"""
powerset([1,2,3]) --> Returns Dictionary where each value is a new distinct subset
"""
def powersets(arr):
  xs=[*arr];D = {}
  for i,x in enumerate(list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))):
    D[i]=x
  return D

def findSubset(S, k):
  D=powersets(S)
  for key in D.keys():
    if(sum(D[key]) == k):
      return sorted([*D[key]])
  return None

S = [12, 1, 61, 5, 9, 2]
k=24
print(findSubset(S, k))
