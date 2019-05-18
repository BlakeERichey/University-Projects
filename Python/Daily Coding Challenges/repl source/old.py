# def packing(*l):
#   print(l)

# def unpacking(x, y, z):
#   print(x, y, z)

# def keywords(a, b, x, y):
#   print(a, b, x, y)

# packing('a', 'b', 'c')
# L = [4,5,6]
# unpacking(*L)

# #keyword arguements
# d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
# keywords(**d)

# def passfunc(demo):
#   demo('passed into passfunc')

# def demo(msg):
#   print(msg)

# passfunc(demo)


# import time
# L = [ [ 9, 10, 11, 12], [ 1,  2,  7, 13], [ 6, 16,  4, 14], [ 3,  8,  5, 15] ]
# import numpy as n;L=l=n.array(L);r,c=[0,3,0,3],136
# f=lambda r:L[r[0]:r[1],r[2]:r[3]]
# while n.any(l):y,x=map(int,n.where(L==n.amax(l)));r=[y-1,y+2,x-1,x+2];r=[max(x,0) for x in r];c-=L[y,x];L[y,x]=0;l=f(r)
# print(c)


# count = 0
# s=list(np.hstack(L)).index(16);s=(s%4,int(s/4))
# s=(s%4,int(s/4))  #current index
# def countCheese(arr):
#   currentIndex = (0,0)
#   for r, row in enumerate(arr):
#     for i, val in enumerate(row):
#       if val == 16:
#         currentIndex = (i, r)
#   print(currentIndex)
#   left = ( currentIndex[0]-1 , currentIndex[1] )
#   right = (currentIndex[0] + 1,currentIndex[1])
#   down = (currentIndex[0],currentIndex[1]+1)
#   up = (currentIndex[0],currentIndex[1] - 1)
#   print("left", left)
#   print('right', right)
#   print('down', down)
#   print('up', up)

# countCheese(L)



# import random, statistics

# def roll():
#   return random.choice(range(1,7))

# def getAttribute():
#   rolls = []
#   for i in range(0,4):
#     rolls.append(roll())
#   rolls.remove(min(rolls))
#   return rolls

# def getCharacterStats():
#   stats = []
#   for i in range(0, 6):
#     stats.append(sum(getAttribute()))
#   return stats

# count = 1
# stats = getCharacterStats()
# while statistics.mean(stats)<13:
#   count+=1
#   stats = getCharacterStats()
# print(stats, "AVG:", statistics.mean(stats), "Rolls", count)

#dex con wis str

# s=''.join([chr(x+97) for x in range(26)])
# print(s)

# stilts => stlilts   //1
# google => elgoogle  //2
# hannah => hannah    //0
# club   => bulclub   //3
# parras => sparraps  //2

# x,y=3,4
# print((0, 8)[6>y>=x>2])

# print(8>>x)

# arr2 = [2,2,3,2,3,5,3]   #5
# arr  = [6,1,6,6,13,13,13] #1

# def findSingle(L):
#   for val in L:
#     if L.count(val) != 3:
#       return val

# print(findSingle(arr2))

# class Greeting:

#   def __init__(self, msg):
#     self.msg=msg

#   def __str__(self):
#     return ''.join(map(chr, map(int, self.msg.split(','))))

# L = '87,101,108,99,111,109,101,33,32,72,111,112,101,32,121,97,108,108,32,108,105,107,101,32,105,116,32,104,101,114,101,33'
# print(Greeting(L))

# print(*L.split(','))


# s = "test"
# import re
# rx=re.compile('[^a-zA-Z]');s=s.split(' ');D={}
# for i, val in enumerate(s):
#  s[i]=rx.sub('', val).lower()
# for val in s:
#  if val not in D.keys():
#   D[str(val)]=s.count(val)
# D=sorted(D.items(),key=lambda v:v[1],reverse=True)
# for t in D:
#   print(str(t[1]) + ":", t[0])

#Out: 'abdE'


# """
# powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
# """
# S = [12, 1, 61, 5, 9, 2]
# k=24
# from itertools import chain, combinations
# D={};r=None
# for i,x in enumerate(list(chain.from_iterable(combinations([*S],n) for n in range(len([*S])+1)))):D[i]=x
# for key in D.keys():
#  if(sum(D[key])==k):
#   r=sorted([*D[key]])
# print(r)
  
# class RunningMedian():
#   def __init__(self):
#     self.vals=[]
#     self.size=0
  
#   def add(self,newVal):
#     self.vals.append(newVal)
#     self.vals=sorted(self.vals)
#     self.size+=1
#     length=self.size
#     if length%2:
#       return (self.vals[int(length/2)])
#     else:
#       index=int(length/2)
#       return (self.vals[index]+self.vals[index-1])/2
# L=[2, 1, 5, 7, 2, 0, 5]
# start=RunningMedian()
# for x in L:
#   print(start.add(x))

# L = [
#   ['usd',  'cda',   1.343020],
#   ['usd', 'euro',   0.894595],
#   ['usd',  'jpn', 109.817182],
#   ['usd',  'chi',    6.88131],
#   ['usd',  'aud',   1.448947],
#   ['cda' , 'usd',    0.744834],
#   ['euro', 'usd',    1.117824],
#   ['jpn' , 'usd',    0.009102],
#   ['chi' , 'usd',    0.145325],
#   ['aud' , 'usd',    0.690279],
# ]

# for x in L:
#   if 

# import requests
# import pandas as pd
# import lxml.html as lh

# url='http://pokemondb.net/pokedex/all'
# page = requests.get(url)
# #Store the contents of the website under doc
# doc  = lh.fromstring(page.content)
# #Parse data that are stored between <tr>..</tr> of HTML
# tr_elements = doc.xpath('//tr')
# #Check the length of the first 12 rows
# #print([len(T) for T in tr_elements[:12]])

# #Parse Header
# #Create empty list
# col=[]
# i=0
# #For each row, store each first element (header) and an empty list
# for ele in tr_elements[0]:
#   i+=1
#   name=ele.text_content()
#   print(i,name)
#   col.append((name,[]))

# ##Fill in rest of table
# #Since out first row is the header, data is stored on the second row onwards
# for j in range(1,len(tr_elements)):
#   #T is our j'th row
#   T=tr_elements[j]
  
#   #If row is not of size 10, the //tr data is not from our table 
#   # if len(T)!=10:
#   #     break
  
#   #i is the index of our column
#   i=0
  
#   #Iterate through each element of the row
#   for t in T.iterchildren():
#     data=t.text_content() 
#     #Check if row is empty
#     if i>0:
#     #Convert any numerical value to integers
#       try:
#         data=int(data)
#       except:
#         pass
#     #Append the data to the empty list of the i'th column
#     col[i][1].append(data)
#     #Increment i for the next column
#     i+=1
# Dict={title:column for (title,column) in col}
# df=pd.DataFrame(Dict)
# print(df.head)
# print('done')


# page = requests.get('https://paradiseposportal.com/agent/list')
# tree = lh.fromstring(page.content)
# #This will create a list of buyers:
# print(tree)
# print('done')

# states = [
#   ['Alabama',        'AL'],
#   ['Alaska',         'AK'],
#   ['Arizona',        'AZ'],
#   ['Arkansas',       'AR'],
#   ['California',     'CA'],
#   ['Colorado',       'CO'],
#   ['Connecticut',    'CT'],
#   ['Delaware',       'DE'],
#   ['Florida',        'FL'],
#   ['Georgia',        'GA'],
#   ['Hawaii',         'HI'],
#   ['Idaho',          'ID'],
#   ['Illinois',       'IL'],
#   ['Indiana',        'IN'],
#   ['Iowa',           'IA'],
#   ['Kansas',         'KS'],
#   ['Kentucky',       'KY'],
#   ['Louisiana',      'LA'],
#   ['Maine',          'ME'],
#   ['Maryland',       'MD'],
#   ['Massachusetts',  'MA'],
#   ['Michigan',       'MI'],
#   ['Minnesota',      'MN'],
#   ['Mississippi',    'MS'],
#   ['Missouri',       'MO'],
#   ['Montana',        'MT'],
#   ['Nebraska',       'NE'],
#   ['Nevada',         'NV'],
#   ['New Hampshire',  'NH'],
#   ['New Jersey',     'NJ'],
#   ['New Mexico',     'NM'],
#   ['New York',       'NY'],
#   ['North Carolina', 'NC'],
#   ['North Dakota',   'ND'],
#   ['Ohio',           'OH'],
#   ['Oklahoma',       'OK'],
#   ['Oregon',         'OR'],
#   ['Pennsylvania',   'PA'],
#   ['Rhode Island',   'RI'],
#   ['South Carolina', 'SC'],
#   ['South Dakota',   'SD'],
#   ['Tennessee',      'TN'],
#   ['Texas',          'TX'],
#   ['Utah',           'UT'],
#   ['Vermont',        'VT'],
#   ['Virginia',       'VA'],
#   ['Washington',     'WA'],
#   ['West Virginia',  'WV'],
#   ['Wisconsin',      'WI'],
#   ['Wyoming',        'WY'],
# ];

# for x in states:
#   print(x)
# print(len(states))

# name='blake'
# age=23
# print(f'my name is {name} and i am {age*2}
