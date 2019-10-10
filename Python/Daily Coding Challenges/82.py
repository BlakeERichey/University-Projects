# This problem was asked Microsoft.

# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”

filedata = 'Hello world'

def read7(): #basic tester function, can throw an error
  global filedata
  read = filedata[:7]
  filedata = filedata[7:]
  return read

def readN(n):
  read = []
  new  = read7()
  while new and not len(''.join(read)) >= n:
    read.append(new)
    new = read7()
  
  return ''.join(read)[:n]

print(readN(9))