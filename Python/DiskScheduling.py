requests = [86, 147, 91, 177, 94, 150, 102, 175, 130]

def fcfs(vals, state):
  sum = 0
  for val in vals:
    sum += abs(state-val)
    state = val
  return sum

def sstf(vals, state):
  copy = [val for val in vals]
  accum = 0
  while len(copy) > 0:
    closest = minDistance(copy, state)
    accum += distance(closest, state)
    state = closest
    copy.remove(closest)
  return accum

def distance(point1, point2):
  return abs(point1 - point2)

def minDistance(arr, currentVal):
  ans   = arr[0]
  delta = distance(ans, currentVal)
  for val in arr:
    if distance(val, currentVal) < delta:
      ans = val
      delta = distance(val, currentVal)
  return ans

print(fcfs(requests, 143))
print(sstf(requests, 143))