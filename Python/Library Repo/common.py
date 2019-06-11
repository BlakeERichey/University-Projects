#normalizes a set of data between a range
def normalize(data, rangeMin, rangeMax):
  if(rangeMin>rangeMax):
    raise 'Invalid Ranges'
  newVals = []
  maxVal=max(data)
  minVal=min(data)
  for val in data:
    if maxVal-minVal == 0:
      newVals.append(rangeMin)
    else: 
      newVals.append((rangeMax-rangeMin)*(val-minVal)/(maxVal-minVal)+rangeMin)
  return newVals

#returns dictionary containing all subsets from a given iterable
def powersets(iterable):
  from itertools import chain, combinations
  D = {}
  xs = list(iterable)
  # note we return an iterator rather than a list
  comb_list = list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))
  
  for key, val in enumerate(comb_list):
    D[key] = val
  return D