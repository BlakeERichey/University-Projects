import math

#loads a csv into a table and returns the table
def loadcsv(filename):
  with open(filename) as file:
    data = file.read()
    lines = data.splitlines()
    table = []
    for line in lines:
      table.append([x.strip() for x in line.split(',')])
    return table

#Savings, Assets, Income in K, Credit Risk
table = loadcsv('./Data Mining/test.csv')

attribute = 3 #4th column = class attribute
pos = 0
neg = 0
count = float(len(table))
for row in table:
  print(row)
  if row[attribute] == 'Good':
    pos += 1
  else:
    neg += 1

#entropy prior to split
entropy = -pos/count * math.log(pos/count, 2) + -neg/count*math.log(neg/count, 2)
print("Entropy:", entropy)


# ENTROPY ON SPLIT
# split = int(input("Attribute to split on: "))
# values = [] #avaiable options for attribute `split`
# for row in table:
#   currentVal = row[split-1]
#   if currentVal not in values:
#     values.append(currentVal)

# countGood = 0
# countBad = 0
# counts = {}
# for value in values:
#   counts[value] =
# print(values)