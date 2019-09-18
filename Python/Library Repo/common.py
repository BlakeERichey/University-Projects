import io, sys, json
import numpy as np
from   io import StringIO

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

def combinations(iterable, trials):
  '''
    returns all possible combinations including variables in `iterable`
    with exactly `trials` number of instances

    combinations(['h', 't'], 2) -> [('h', 'h'), ('h', 't'), ('t', 'h'), ('t', 't')]
  '''
  import itertools
  return list(itertools.product(iterable, repeat=trials))

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

#rgb = (r, g, b)
def rgb_to_hex(rgb):
  if len(rgb) == 3:
    valid = True
    for val in rgb:
      if not(val != None and type(val) == int and 0<=val<=255):
        valid = False
        break
        
    if valid:
      as_hex = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
    else: #invalid values
      as_hex = '#000000'
    
    return as_hex

def silence_function(func, *args, **kwargs):
  '''
    Replaces stdout temporarily to silence print statements inside a function
  '''
  #mask standard output
  actualstdout = sys.stdout
  sys.stdout   = StringIO()

  try:
    func(*args, **kwargs)
  finally: #set stdout but dont catch error
    sys.stdout = actualstdout

def find_closest(arr, val):
  '''finds closest value in arr to val'''
  vals = arr.tolist()
  distances = [abs(vals[i] - val) for i in range(len(vals))]
  return vals[distances.index(min(distances))]

def save_json(obj, filename):
  '''save obj to filename. obj is expected to be a json format'''
  with open(filename, 'w+') as f:
    json.dump(obj, f)

def load_json(filename):
  '''returns dictionary with json data'''
  with open(filename, 'r') as f:
    obj = json.loads(f.read())
  
    return obj

def flatten(iter):
  '''
    flatten an iterable into a 1d numpy array
  '''
  if type(iter) == dict:
    return np.array(list(iter.values())).reshape(1, -1)[0]
  elif type(iter) == list:
    return np.array(iter).reshape(1, -1)[0]

def get_sums(d):
  '''
    sum `d`, dictionary of list, on col axis into a list
  '''
  i = len(d)
  j = len(list(d.values())[0])
  s = flatten(d)
  return list(np.sum(s.reshape(i, j), axis=0))

  
#--------------------------------Tree Functions--------------------------------

def paths_to_leaves(tree):
  '''
    Calls collect_paths to find all paths from root of a tree to its leaves
  '''
  d = {'paths': []}
  collect_paths(tree.root, [], d)
  return d['paths']


def collect_paths(node, path, d):
  if node:
    path = path + [node.data]
    if node.getLeft() == None and node.getRight() == None:
      d['paths'].append(path)
    else:
      collect_paths(node.getLeft(), path, d)
      collect_paths(node.getRight(), path, d)

def get_next(item_num, dir):
  '''
    returns next node number in tree in dir specified
        0      level: 0
      / \    
      1   2           1
    / \ / \
    3  4 5  6         2

    get_next(2, 'left') => 5
    get_next(1, 'right') => 4 
  '''
  item_num   = int(item_num)
  level, pos = get_level(item_num)
  next_level = pow(2, level+1) #items in next level
  add        = next_level-(pow(2, level)-pos)
  left       = item_num + add
  
  return (left, left+1)[dir=='right']
      
def get_level(curNum):
  '''
    helper function to get level and pos of a number in a binary tree
        0      level: 0
      / \    
      1   2           1
    / \ / \
    3  4 5  6         2

  get_level(2) => 1, 1
  get_level(4) => 2, 1 
  '''
  curNum = int(curNum)
  level = 0
  while pow(2, level+1) <= curNum+1:
    level+=1
  pos = curNum - pow(2, level) + 1 #0 indexed
  return level, pos

def get_parent(curNum):
  '''
   get parent node number from binary tree locations
  '''
  if curNum < 1:
    return None
  return (curNum-1)//2