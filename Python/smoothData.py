import random

#returns standard deviation of a list, arr
def stDev(arr):
  sampleSum = sum(arr)
  meanSample = sampleSum / len(arr)

  sqDiffSum = 0
  for i in range(0, len(arr)):
    sqDiffSum += pow(meanSample - arr[i], 2)
  return pow(sqDiffSum / len(arr), .5)

#bins arr into bins of size binSize. Returns averages
def binData(arr, binSize):
  sample = [] #used to hold bins until average is calculated and pushed into binnedData
  binnedData = [] #result of binning
  copyArr = [x for x in arr]
  while( len(copyArr) > 0 ):
    for i in range(0, binSize):
      if(len(copyArr) > 0):
        sample.append(copyArr.pop())
    avg = sum(sample)/len(sample)
    for i in range(0, len(sample)):
      binnedData.append(avg)
    sample = []
  return binnedData

#takes a binned set of data and removes outliers using 1 StDev as threshold
def smoothByBinning(arr, binSize):
  #-----BIN DATA-----
  binnedData = binData(arr, binSize)

  #-----SMOOTH BY SD-----
  mean = sum(binnedData) / len(binnedData)
  dev = stDev(binnedData)
  newList = []    #smoothed data
  for i in range(0, len(binnedData)):
    if (abs(binnedData[i]-mean) < dev):
      newList.append(binnedData[i])
  return newList

#takes unfiltered data and smooths by removed outliers using 1xStDev as threshold
def smoothBySD(arr):
  dev = stDev(arr)
  mean = sum(arr) / len(arr)
  newList = []
  for i in range(0, len(arr)):
    if (abs(arr[i]-mean) < dev):
      newList.append(arr[i])
  return newList

print( "Goal mean:", 250)

#find sample means, try to reduce noise
def createSample():
  data = []
  for x in range(0, 100):
    add = random.choice([1,3,5,7,11,13,17,23,31,-1,-3,-5,-7,-11,-13,-17,-23,-31])
    data.append(add + 250)
  return data

data = []
run = True
while run:
  data = createSample()
  if(stDev(data) < 12):
    run = False
print( "True mean:", sum(data) / len(data) )

print('-----Smoothing by SD-----')
sdSmooth = smoothBySD(data)
#print('Smoothed Data:', sdSmooth)
print('Smoothed data mean:', sum(sdSmooth) / len(sdSmooth))
print('StdDev of Smoothed Data:', stDev(sdSmooth))

print('-----Binned Data-----')
binnedData = binData(data, 3)
#print(binnedData)
print('Mean:', sum(binnedData) / len(binnedData))
print('StdDev:', stDev(binnedData))

print('-----After Smoothing by Binning-----')
binnedData = smoothByBinning(data, 3)
#print("Binned data:", binnedData)
print("Binned mean:", sum(binnedData) / len(binnedData) )
print("STD DEV Binned data:", stDev(binnedData))

print('-----JUST TRYING STUFF NOW LOL-----')
test = smoothBySD(data)
binnedData = smoothByBinning(test, 3)
print("Binned mean:", sum(binnedData) / len(binnedData) )
print("STD DEV Binned data:", stDev(binnedData))