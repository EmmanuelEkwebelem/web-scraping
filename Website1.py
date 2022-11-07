import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://pubs.rsna.org/toc/radiology/304/3'
page = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())


Category = soup.find_all('span',class_='badge-type')
Categorys = []
for item in Category:
    C = item.text 
    C = C.strip()   
    C = C.replace('\n','')
    C = C.replace('Free','')
    C = C.replace('Open Access','')
    Categorys.append(C)
len(Categorys)
while("" in Categorys):
    Categorys.remove("")
print(len(Categorys))

Title = soup.find_all('h5',class_='issue-item__title')
Titles = []
for item in Title:
    T = item.text 
    T = T.strip()   
    T = T.replace('\n','')
    T = T.replace(' ','')
    Titles.append(T)
len(Titles)
print(len(Titles))

Article_Author = soup.find_all('ul',class_='rlist--inline loa')
Article_Authors = []
for item in Article_Author:
    AU = item.text 
    AU = AU.strip()   
    AU = AU.replace('\n','')
    Article_Authors.append(AU)
len(Article_Authors)
print(len(Article_Authors))

list1 = Categorys
list2 = Titles
list3 = Article_Authors

df = pd.DataFrame({'Article Class': list1, 'Article Titles': list2, 'List of Article Author Names': list3})
df.to_csv('Data/Website1.csv')