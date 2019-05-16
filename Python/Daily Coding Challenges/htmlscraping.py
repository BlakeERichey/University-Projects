import requests
import pandas as pd
import lxml.html as lh

url='http://pokemondb.net/pokedex/all'
page = requests.get(url)
#Store the contents of the website under doc
doc  = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
#Check the length of the first 12 rows
#print([len(T) for T in tr_elements[:12]])

#Parse Header
#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for ele in tr_elements[0]:
  i+=1
  name=ele.text_content()
  print(i,name)
  col.append((name,[]))

##Fill in rest of table
#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
  #T is our j'th row
  T=tr_elements[j]
  
  #If row is not of size 10, the //tr data is not from our table 
  # if len(T)!=10:
  #     break
  
  #i is the index of our column
  i=0
  
  #Iterate through each element of the row
  for t in T.iterchildren():
    data=t.text_content() 
    #Check if row is empty
    if i>0:
    #Convert any numerical value to integers
      try:
        data=int(data)
      except:
        pass
    #Append the data to the empty list of the i'th column
    col[i][1].append(data)
    #Increment i for the next column
    i+=1
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
print(df.head)
print('done')


# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = lh.fromstring(page.content)
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')
# print(buyers)
# print('done')
