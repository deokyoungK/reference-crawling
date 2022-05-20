import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#만화제목 + 링크가져오기
#cartoons = soup.find_all('td',attrs={'class':'title'})
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com'+cartoon.a['href']
#     print(title, link)


#평점 구하기
total_rate = 0
ratings = soup.find_all('div',attrs={'class':'rating_type'})
for rating in ratings:
    rate = rating.find("strong").get_text()
    total_rate += float(rate)

print("전체 점수: ",total_rate)
print("평균 점수: ",total_rate/len(ratings))


