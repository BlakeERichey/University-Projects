from itertools import combinations

def multiplyList(arr):
  result = 1
  for val in arr:
    result *= val
  return result
  
L = [10, 6, -3, 15, -10, 7, 7, -15]
assert len(L)>2
options = list(combinations(L, 3))
curMax  = {'value': multiplyList(options[0]), 'list': options[0]}

for tup in options:
  maxVal = curMax['value']
  newVal = multiplyList(tup)
  if newVal > maxVal:
    curMax.update({'value': newVal, 'list': tup})

print(curMax['value'])