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

#removes imprecision issues with floats: 1-.1 = .900000000001 => 1-.1 = .9
def truncate_number(f_number, n_decimals=9):
  strFormNum = "{0:." + str(n_decimals+5) + "f}"
  trunc_num  = float(strFormNum.format(f_number)[:-5])
  return(trunc_num)

#rounds number to the nearest value `nearest`
#`nearest` must be between 0-1
def round_nearest(number, nearest=.05):
  lower  = number // 1 #lower limit
  upper  = lower +1    #upper limit

  values = []          #possible values
  curVal = lower
  while curVal <= upper:
    values.append(curVal)
    curVal=truncate_number(curVal + nearest)
  
  if upper not in values:
    values.append(upper)
  
  distance = []        #distance to each possible value
  for value in values:
    distance.append(abs(number-value))
  print(values)
  return values[distance.index(min(distance))]