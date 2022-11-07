import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.academicradiology.org/inpress'
page = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
soup.prettify()

Title = soup.find_all('h3',class_='toc__item__title')
Titles = []
for item in Title:
    T = item.text 
    T = T.strip()   
    T = T.replace('\n','')
    Titles.append(T)
len(Titles)
print(len(Titles))

Article_Author = soup.find_all('ul',class_='toc__item__authors loa rlist--inline')
Article_Authors = []
for item in Article_Author:
    AU = item.text 
    AU = AU.strip()   
    AU = AU.replace('\n','')
    Article_Authors.append(AU)
len(Article_Authors)
print(len(Article_Authors))

Pub_Date = soup.find_all('div',class_='toc__item__date')
Pub_Dates = []
for item in Pub_Date:
    C = item.text 
    C = C.strip()   
    C = C.replace('\n','')
    C = C.replace('Published Online: ','')
    Pub_Dates.append(C)
len(Pub_Dates)
print(len(Pub_Dates))

list1 = Titles
list2 = Article_Authors
list3 = Pub_Dates

df = pd.DataFrame({'Article Titles': list1, 'List of Article Author Names': list2, 'Publication Dates': list3})
df['Publication Dates'] = df['Publication Dates'].str.replace('Published online: ', '')
df.to_csv('Data/Website2.csv')