class CSV():
  def __init__(self, data):
    self.string=('', data)[data!=None]
  
  def add(self, arr):
    for x in arr:
      self.string+=f'\"{x}\",'
    self.eol()
  
  def eol(self):
    self.string=self.string[:-1] + '\n'#remove comma

  def __str__(self):
    return self.string
  
  def loadFromFile(self, filename):
    with open(filename) as file:
      data = file.read()
      lines = data.splitlines()
      table = []
      for line in lines:
        table.append([x.strip() for x in line.split(',')])
      return table
  
  #takes CSV object and returns parsed as an array
  def load(self):
    lines = self.string.splitlines()
    table = []
    for line in lines:
      table.append([x.strip() for x in line.split(',')])
    return table
  
  def save(self, filename):
    with open(filename, 'w') as file:
      file.write(self.string)