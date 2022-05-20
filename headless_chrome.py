import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)

#페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=US"
browser.get(url)

#지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,2080)")

#화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
interval = 2

#현재 문서높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행
while True:
    #스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    #페이지 로딩 대기
    time.sleep(interval)
    
    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if(curr_height == prev_height):
        break

    prev_height = curr_height
    
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

###############
#selenium을 이용해서 동적페이지를 로드했다.

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs={"class":"WHE7ib mpg5gc"})
print(len(movies))
for movie in movies:

    #영화 제목
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    
    #할인 후 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    #링크
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    #올바른링크: https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com"+link)
    print("-"*100)

browser.quit()