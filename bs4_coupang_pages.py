#쿠팡은 페이지이동이 get방식으로 이루어지기때문에 
#스크래핑하기 쉽다.
#크롤링과정에서 잘 안될수있다 -> selenium필요..

import requests
import re #정규식사용
from bs4 import BeautifulSoup

for i in range(1,6):
    print("페이지: ",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    items = soup.find_all('li',attrs={'class':re.compile('^search-product')})
    for item in items:

        name = item.find('div',attrs={'class':'name'}).get_text()
        #HP제품 제외
        if 'HP' in name:
            continue
        price = item.find('strong',attrs={'class':'price-value'}).get_text()
        
        #평점 4.5이상, 리뷰 100개 이상만 조회
        rating = item.find('em',attrs={'class':'rating'})
        if rating:
            rating = rating.get_text()
        else:
            continue

        rating_cnt = item.find('span',attrs={'class':'rating-total-count'})
        if rating_cnt:
            rating_cnt = rating_cnt.get_text()[1:-1] #예 (26)
        else:
            continue

        link = item.find("a",attrs={'class':'search-product-link'})['href']
        if float(rating)>=4.5 and int(rating_cnt)>=100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rating}점 ({rating_cnt}개)")
            print("바로가기 : ",format("https://www.coupang.com" + link))
            print('-'*100)




