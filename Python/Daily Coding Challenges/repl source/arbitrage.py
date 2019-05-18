# import requests
# import lxml.html as lh

# def getTable(msg):
#   url='https://www.x-rates.com/table/?from=' + msg + '&amount=1'
#   page = requests.get(url)
#   doc  = lh.fromstring(page.content)
#   #Parse data that are stored between <tr>..</tr> of HTML
#   tr_elements = doc.xpath('//tr')

#   headers=[]
#   #Parse Titles of Columns
#   for i,ele in enumerate(tr_elements[0]):
#     name=ele.text_content()
#     headers.append(name)
#   #print('headers', headers)

#   ##Fill in rest of table
#   table=[]
#   for j in range(1,len(tr_elements)):
#     row=tr_elements[j]
    
#     if len(row)!=3:
#       break
#     #Iterate through each element of the row
#     tds=row.iterchildren()
#     data=[td.text_content() for td in tds]
#     for i,td in enumerate(data):
#       try:
#         data[i]=float(td)
#       except:
#         pass
#     data.insert(0, headers[0])
#     table.append(data)
#   return table

# ##GENERATE TABLES
# allTables = [];arbitrages=[]
# currencies=['USD', 'JPY', 'EUR', 'INR', 'AUD']
# for currency in currencies:
#   allTables+=getTable(currency)

# #FIND ARBITRAGES
# for trade in allTables:
#   try:
#     if trade[2]*trade[3]>1.0099:
#       arbitrages.append(trade)
#   except:
#     pass
# for x in arbitrages:
#   print(x, x[2]*x[3])
# print('done')