import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인버튼클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. 틀린id, pw입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("fhemfrpt1")


#4. 로그인 버튼클릭
browser.find_element_by_id("log.login").click()

time.sleep(2)

#5. id를 다시 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("kang48450")

#6. html정보 출력
print(browser.page_source)


