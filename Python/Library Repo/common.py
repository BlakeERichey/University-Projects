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

L=[0,0,0,0]
print(normalize(L, 6, 5))
