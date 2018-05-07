# 패키지 로드

import urllib.request, urllib.parse, urllib.error
import json

# google map api 변수 설정 json 으로

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# 입력 주소가 없으면 break 아니면 무한 루프

while True:
    
    address = input('Enter location: ')
    
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    
    # url 변수에 저장    
    uh = urllib.request.urlopen(url)
    
    # 읽을 수 있는 형태로 decode
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    # 로드가 잘 안됬을 시 출력하는 문장, 로드 성공시 continue
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # 위도와 경도를 로드한 json 파일에서 추출하는 코드
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    
    # 주소 추출
    location = js['results'][0]['formatted_address']
    print(location)
