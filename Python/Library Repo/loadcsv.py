#loads a csv into a table and returns the table
def loadcsv(filename):
  with open(filename) as file:
    data = file.read()
    lines = data.splitlines()
    table = []
    for line in lines:
      table.append([x.strip() for x in line.split(',')])
    return table