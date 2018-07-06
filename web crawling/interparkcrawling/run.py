# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 18:11:12 2018

@author: cdh66
"""

#모듈로드
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
#명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DbMgr import DBHelper as Db
import pymysql as my
import time


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from Tour import TourInfo

#인터파크 홈페이지
db = Db()
main_url = 'http://fly.interpark.com/'
keyword = '파리'
# 사품 정보를 담는 리스트
tour_list = []

#드라이버로드
driver = wd.Chrome('e:/chromedriver/chromedriver.exe')

#사이트 접속
driver.get(main_url)

#id : SearchGNBText

driver.find_element_by_id('SearchGNBText').send_keys(keyword)

#검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

#잠시 대기


try:
    element = WebDriverWait(driver,10).until(
            #지정한 한개 요소가 올라오면 웨이트 종료
            EC.presence_of_element_located((By.CLASS_NAME,'oTravelBox'))
            )
except Exception as e:
    print('오류 발생',e)
# 요소를 찾을 특정 시간 동안 DOM 풀링 지시 10초
driver.implicitly_wait(10)
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

#게시판에서 데이터 가져올때
#데이터가 많으면 세션 관리
#특정 단위별로 로그아웃 로그인 계속 시도
#특정 게시물이 사라질 경우 팝업 발생
#게시판 스캔 -> 메타 정보 흭득 -> loop 를 돌려서 일괄적 처리

#searchModule.SetCategoryList(1, '') 스크립트 실행
for page in range(1,2):
    try:

        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(2)
        ####################
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 섬네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
        # 상품 하나하나 접근
        for li in boxItems:
            print('섬네일',li.find_element_by_css_selector('img').get_attribute('src'))
            print('링크',li.find_element_by_css_selector('a').get_attribute('onclick'))
            print('상품명',li.find_element_by_css_selector('h5.proTit').text )
            print('코멘트',li.find_element_by_css_selector('.proSub').text )
            print('가격',li.find_element_by_css_selector('.proPrice').text )

            for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                print(info.text)
            print('='*100)
            #데이터 모음
            #데이터가 부족하거나 없을수도 있으므로 직접 인덱스로 표현은 위험성이 있음
            obj = TourInfo(
            li.find_element_by_css_selector('h5.proTit').text,
            li.find_element_by_css_selector('.proPrice').text,
            li.find_elements_by_css_selector('.info-row .proInfo')[1].text,
            li.find_element_by_css_selector('a').get_attribute('onclick'),
            li.find_element_by_css_selector('img').get_attribute('src'))
            tour_list.append(obj)

    except Exception as e1:
        print('오류',e1)

print(tour_list,len(tour_list))

for tour in tour_list:
    print(type(tour))
    # 링크 데이터에서 실데이터 흭득
    arr = tour.link.split(',')
    if arr:
        link = arr[0].replace('searchModule.OnClickDetail(','')
        detail_url = link[1:-1]

        #상세 페이지 이동
        driver.get(detail_url)
        time.sleep(2)
        #현재 페이지를 BeautifulSoup 의 DOM 으로 구성
        soup = bs(driver.page_source,'html.parser')
        #현재 상세 저보 페이지에서 스케줄 정보 흭득
        data = soup.select('.tip-cover')
        print(type(data), len(data))
        # 디비 입력
        content_final = ''
        for c in data[0].contents:
            content_final = str(c)

        db.db_insertcrawlingdata(tour.title,
                    tour.price,
                    tour.area,
                    content_final,
                    keyword
        )
# 종료
driver.close()
driver.quit()
import sys
sys.exit()
