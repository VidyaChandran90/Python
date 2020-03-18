import bs4
import requests
import lxml
import pandas as pd
'''
res=requests.get('https://en.wikipedia.org/wiki/Harry_Potter')
#print(res.text)

soup=bs4.BeautifulSoup(res.text,'lxml')
#print(type(soup))
#var1=soup.select('class="plainlist"')

My_table = soup.find('table',{'class':'infobox'})
#print(My_table)
links=My_table.find_all('a')
#print(links)

Harry_Series=[]
for link in links:
    if link.get('href').find('/wiki/Harry_')==-1:
        pass
    else:
        #print(link.get('href'))
        Harry_Series.append(link.get('title'))

#print(Harry_Series)
df=pd.DataFrame()
df['Harry_Series']=Harry_Series
print('\n\nHarry Potter Series')
print(df)


res1=requests.get('https://en.wikipedia.org/wiki/Friends')
soup1=bs4.BeautifulSoup(res1.text,'lxml')
My_table1=soup1.find('table',{'class':'wikitable plainrowheaders'})
#print(My_table1)
links1=My_table1.find_all('a')
Friends=[]
for lnk in links1:
    if lnk.get('title') is None:
        txt='NOTEXT'
    else:
        txt=lnk.get('title')

    if txt.find('The')==-1:
        pass
    else:
        Friends.append(lnk.get('title'))

df1=pd.DataFrame()
df1['Friends']=Friends
print('\n\nFriends Most Watched Episodes')
print(df1)
'''


res2=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup2=bs4.BeautifulSoup(res2.text,'lxml')
My_table2=soup2.select('.toc')
#print(My_table2)
for i in My_table2:
    if i.text.strip() is None:
        continue
    else:
        print(i.text)
'''
links1=My_table2.find_all('a')
Friends=[]
for lnk in links1:
    if lnk.get('title') is None:
        txt='NOTEXT'
    else:
        txt=lnk.get('title')

    if txt.find('The')==-1:
        pass
    else:
        Friends.append(lnk.get('title'))

df1=pd.DataFrame()
df1['Friends']=Friends
print('\n\nFriends Most Watched Episodes')
print(df1)
'''
