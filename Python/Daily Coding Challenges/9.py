def maxSum(arr, i = 0):
  sum = arr[i] + arr[i+2] + arr[i+4]
  print(sum)

maxSum([1,2,3,4,5])