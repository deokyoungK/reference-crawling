import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
#print(soup.a['href'])

# print(soup.find('a',attrs={"class":"Nbtn_upload"}).get_text())
#rank1 = soup.find('li',attrs={'class':'rank01'})
# print(rank1.a.get_text())
# rank2 = rank1.find_next_sibling('li')
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())

#print(rank1.find_next_siblings('li'))



