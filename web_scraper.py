import requests
from bs4 import BeautifulSoup

# 웹페이지 URL
url = 'https://httpbin.org'  # 여기에 실제 웹페이지 URL을 입력하세요.

# HTTP 요청을 보내고 응답을 받습니다.
response = requests.get(url)

# 응답의 HTML 내용을 BeautifulSoup으로 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 <p> 태그를 추출하는 경우:
for paragraph in soup.find_all('p'):
    print(paragraph.text)

# 또는 클래스명이 'example-class'인 모든 <div> 태그를 추출하는 경우:
for div in soup.find_all('div', class_='example-class'):
    print(div.text)

# 선택한 데이터를 파일에 저장할 수도 있습니다.
with open('output.txt', 'w', encoding='utf-8') as file:
    for paragraph in soup.find_all('p'):
        file.write(paragraph.text + '\n')
