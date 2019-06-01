from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

#카페에서 chromedriver 다운로드
# 환경설정이 이상한지 파이참의 터미널에서 안될경우  C:\ProgramData\Anaconda3\Scripts 위치에서 pip install selenium 실행



class NaverMovie:
    def __init__(self, url):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # 한줄코딩 driver, 컨트롤 스페이스
        print(soup)
