def swapverse(a,b):
  '''
    swaps a and b and reverses them

    Example:
    >>>a = [1,2,3,4]
    >>>b = [5,6,7,8]
    >>>swapverse(a,b)
    >>>print(a)
    >>>[8,7,6,5]
    >>>print(b)
    >>>[4,3,2,1]
    
    Difficulty: 1.5
  '''
  pass

def argmax(arr):
  '''
    finds the index of a one/two dimensional array
    that corresponds to the maximum value for each array

    Example:
    >>>a = [2,1,3,5]
    >>>b = [
        [6,3,5],
        [3,4,9],
        [4,7,5],
      ]
    >>>argmax(a)
    >>>3
    >>>argmax(b)
    >>>[0,2,1]

    Difficulty: 1.5
  '''
  pass

def generate_ccnum(qty=1):
  '''
    using the luhn algorithm to validate credit card numbers
    generates a number of valid credit card numbers equal to `qty`
    
    Difficulty: 2.5
  '''
  pass

def mystery():
  '''
    No use of computer for this problem!!!
    Question: What is the output?
    >>>print(mystery())
    >>>???

    Difficulty: 2
  '''
  arr = [3,1,9,2,8,6,7,5]

  arr1 = []
  arr2 = []
  for _ in range(len(arr)):
    temp = arr.pop()
    
    if len(arr1) != len(arr2):
      insert_into = arr2
    else:
      insert_into = arr1
    
    i = 0
    for val in insert_into:
      if val > temp:
        break
      i+=1
    
    insert_into.insert(i, temp)
  
  return arr1, arr2

def binData(arr, binSize):
  '''
    Question: Find the error!
    
    bins arr into bins of size binSize. averaging the numbers in the bins

    >>>binData([1,1,10], 3)
    >>>[4.0,4.0,4.0]

    >>>binData([1,1,99,2,3,100,16,16,18], 3)
    >>>[33.66,33.66,33.66,35.0,35.0,35.0,16.66,16.66,16.66]

    Difficulty: 3
  '''
  sample = [] #used to hold bins until average is calculated and pushed into binnedData
  binnedData = [] #result of binning
  copyArr = [x for x in arr]
  while( len(copyArr) > 0 ):
    #bin numbers up to bin size
    for i in range(0, binSize):
      if(len(copyArr) > 0):
        sample.append(copyArr.pop())
    
    #calculates avg of binSize measurements
    avg = sum(sample)/len(sample)
    
    #adds avg to binndedData len(sample) times
    for i in range(0, len(sample)):
      binnedData.append(avg)

  return binnedData[::-1]


class Blob:

  '''
    Blobs are the building blocks for an upcoming Genetic Algorithm
    A blob has a color, and an age

    Available colors are: Red, Green, Yellow
    Blobs always start at age 0

    The Blob class allows for creation of blobs and aging of blobs.

    Difficulty: 3
  '''

  def __init__(self,):
    pass
  
  def age(self,chance_of_death = .5):
    '''
      ages a blob one year older with a chance of death = `chance_of_death`
      
      Blobs who are dead do not get older. 
      Thus once a blob dies, it remains the same age every year afterward.
    '''
    pass
  
  def __str__(self,):
    '''
      When printed, should print the status of the blob including:
      1) How old the blob is
      2) If the blob is dead, how long has the blob been dead
      3) What color the blob is
    '''
  
    pass