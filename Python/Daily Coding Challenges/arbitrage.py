from BRQueue import Queue

from itertools import chain, combinations
"""
powerset([1,2,3]) --> Returns Dictionary where each value is a new distinct subset
"""
def powersets(arr):
  xs=[*arr];D = {}
  for i,x in enumerate(list(chain.from_iterable(combinations(xs,n) for n in range(4)))):
    D[i]=x
  return D

import requests
import lxml.html as lh

def getTable(msg):
  url='https://www.x-rates.com/table/?from=' + msg + '&amount=1'
  page = requests.get(url)
  doc  = lh.fromstring(page.content)
  #Parse data that are stored between <tr>..</tr> of HTML
  tr_elements = doc.xpath('//tr')

  headers=[]
  #Parse Titles of Columns
  for i,ele in enumerate(tr_elements[0]):
    name=ele.text_content()
    headers.append(name)
  #print('headers', headers)

  ##Fill in rest of table
  table=[]
  for j in range(1,len(tr_elements)):
    row=tr_elements[j]
    
    if len(row)!=3:
      break
    #Iterate through each element of the row
    tds=row.iterchildren()
    data=[td.text_content() for td in tds]
    for i,td in enumerate(data):
      try:
        data[i]=float(td)
      except:
        pass
    data.insert(0, headers[0])
    table.append(data)
  return table

##GENERATE TABLES
allTables = [];arbitrages=[]
currencies=['USD', 'JPY', 'EUR', 'INR', 'AUD']
for currency in currencies:
  allTables+=getTable(currency)

#FIND ARBITRAGES
for trade in allTables:
  try:
    if trade[2]*trade[3]>1.0099:
      arbitrages.append(trade)
  except:
    pass
print('Calculating...')
for x in arbitrages:
  print(x, x[2]*x[3])

print('Generating Subpaths...')
D=powersets(allTables);subpaths=[]
i=0
print('Looking at subpaths...')
for subpath in D:
  while i == 0:
    subqueue=Queue();valid=True
    subqueue.enqueue(D[subpath])
    print(subqueue.getList())
    for i in range(len(D[subpath])-1):
      first = subqueue.dequeue()
      if not(first and first[1] == subqueue.front[0]):
        valid=False
    i+=1

print('done')
