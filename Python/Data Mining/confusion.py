# Blake Richey
# Data Mining 4352 - 001, Spring 2019
# Dr Kulkarni
# take in confusion matrix and display accuracy, error rate, sensativity, 
# specificity, precision, F-Score, and FPR

#formats a percentage as a friendly readable number
#precision: number of decimals to include
def formatPercentage(num, precision):
  if num == 0:
    return 0
  numAsStr = str(num)
  decimalLocation = numAsStr.index('.')
  return float(numAsStr[0:decimalLocation+precision+1]) #4 decimals of precision

#finds values of accuracy, error rate. etc of a passed in cofusion matrix
def classify(matrix):

  classifier = int(input("Enter class to get results (1, 2, 3...): ")) #class to find values on
  if(classifier > len(matrix)):
    return "Invalid Entry"
  
  #GENERATE 2D CONFUSION MATRIX
  classifierMatrix = [[], []]
  classifierMatrix[0].append(matrix[classifier-1][classifier-1])  #correctly classified as classifier

  currentVal = 0  #value to add to 2d matrix
  for i, val in enumerate(matrix[classifier-1]):
    if i != classifier-1:
      currentVal += val
  classifierMatrix[0].append(currentVal) #guess was not classifier but really was

  currentVal = 0
  for i in range((len(matrix))):
    val = matrix[i][classifier-1]
    if i != classifier - 1:
      currentVal+= val
  classifierMatrix[1].append(currentVal) #guessed was classifier but was really not

  samples = 0
  for i in range(len(matrix)):
    samples += sum(matrix[i])
  currentSum = classifierMatrix[0][0] + classifierMatrix[0][1] + classifierMatrix[1][0]
  classifierMatrix[1].append(samples - currentSum) #was not classifier and correctly guess was not

  #FIND VALUES
  accuracy    = (classifierMatrix[0][0] + classifierMatrix[1][1]) / float(samples)
  errorRate   = 1-accuracy
  sensativity = classifierMatrix[0][0] / float(classifierMatrix[0][0] + classifierMatrix[0][1])
  specificity = classifierMatrix[1][1] / float(classifierMatrix[1][0] + classifierMatrix[1][1])
  precision   = classifierMatrix[0][0] / float(classifierMatrix[0][0] + classifierMatrix[1][0])
  fScore      = 2 * precision * sensativity / float(precision + sensativity)
  fpr         = 1-specificity

  results = {}
  results["Accuracy:"]    = formatPercentage(accuracy,    4)
  results["Error Rate:"]  = formatPercentage(errorRate,   4)
  results["Sensativity:"] = formatPercentage(sensativity, 4)
  results["Specificity:"] = formatPercentage(specificity, 4)
  results["Precision:"]   = formatPercentage(precision,   4)
  results["Fscore:"]      = formatPercentage(fScore,      4)
  results["Fpr:"]         = formatPercentage(fpr,         4)
  return results

def main():
  #Confusion Matrix (Change this value to make further tests)
  matrix = [
    [28, 2, 3],
    [5, 39, 0],
    [1, 6, 18]
  ]

  values = classify(matrix)

  for entry in values:
    print(entry, values[entry])

main()