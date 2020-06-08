import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "file:///C:/Users/darsh/Desktop/web.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


house_rate = soup.find_all('div',class_ = "css-yya0yl")

#print("res -",len(house_rate))

#TYPE OF HOUSE i.e. 1BHK OR 2BHK
config_of_house = []
for first in house_rate:

    Config = first.find('div',class_ = "css-1ty8tu4")
    config = re.findall('>([^*]+)',str(Config))
    for x in config:
        con = x[0:len(x)-6]
        config_of_house.append(con)

#print(len(config_of_house))

#FOR GETTING THE AREA OF THE FLAT
area_list = []
for first in house_rate:
    Area = first.find_all('a',class_ = "css-fwbz9r")
    #print(area)
    for x in Area:
        area = re.findall('>([^*]+)',str(x))
        #print(area)
        for x in area:
            a = x[0:len(x)-4]
            area_list.append(a)
            #print(a)
#print(len(area_list))


#FOR GETTING THE PRICE OF ALL THE FLATS
price_list = []
for first in house_rate:
    Price = first.find_all('h2')

    for x in Price:
        price = re.findall('<h2 class="css-yr18fa">([^*]+)',str(x))
        #print(price)
        for x in price:
            if(x[0] == "P"):
                p = x[0:len(x)-5]
                price_list.append(p)
            else:
                p = x[1:len(x)-5]
                price_list.append(p)

#print(price_list)

#FOR GETTING THE DEVELOPERS
# developers_list = []
# for first in house_rate:
#     Developer = first.find_all('div',class_ = "css-1j62xqm")
#     #print(Developer)

#     for x in Developer:
#         dev = re.findall('-->([^*]+)',str(x))
#         for x in dev:
#             d = x[9:len(x)-6]
#             developers_list.append(d)
# print(developers_list)


#FOR GETTING BUILDING NAMES
building_name_list = []
for first in house_rate:
    Building = first.find_all('a',class_ = "css-163eyf0")
    #print(Building)

    for x in Building:
        bui = re.findall('">([^*]+)',str(x))
        
        for x in bui:
            building = x[0:len(x)-4]
            building_name_list.append(building)
#print(len(building_name_list))



import pandas as pd

df = pd.DataFrame({
    "Area":area_list,
    "Type":config_of_house,
    "Price":price_list,
    "Apartment Name":building_name_list
})

print(df.head(5))
df.to_csv("palghar_price_list.csv")
