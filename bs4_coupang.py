#쿠팡은 페이지이동이 get방식으로 이루어지기때문에 
#스크래핑하기 쉽다.


import requests
import re #정규식사용
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=5&backgroundColor='
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all('li',attrs={'class':re.compile('^search-product')})
for item in items:

    #광고제품 제외
    ad_badge = item.find('span',attrs={'class':'ad-badge-text'})
    if ad_badge:
        print("<광고상품 제외합니다>")
        continue

    name = item.find('div',attrs={'class':'name'}).get_text()
    #HP제품 제외
    if 'HP' in name:
        print("<HP 상품 제외합니다>")
        continue
    price = item.find('strong',attrs={'class':'price-value'}).get_text()
    
    #평점 4.5이상, 리뷰 100개 이상만 조회
    rating = item.find('em',attrs={'class':'rating'})
    if rating:
        rating = rating.get_text()
    else:
        print("<평점 없는 상품입니다>")
        continue

    rating_cnt = item.find('span',attrs={'class':'rating-total-count'})
    if rating_cnt:
        rating_cnt = rating_cnt.get_text() #예 (26)
        rating_cnt = rating_cnt[1:-1]
    else:
        print("<평점 수 없는 상품입니다>")
        continue

    if float(rating)>=4.5 and int(rating_cnt)>=100:
        print(name, price, rating, rating_cnt)




