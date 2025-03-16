# https://github.com/keyfrog-21K/lunch-igbot.git
# main.py

import os
from pathlib import Path

from dotenv import load_dotenv
from instagrapi import Client
import schedule
import datetime
import time

# 모듈 불러오기
from meal_loader import meal_loader
from image_generator import create_image_with_template


# 초기 시작 및 로그인 프로세스
print('프로그램이 성공적으로 시작되었습니다.')

load_dotenv()
ig_id = os.getenv('INSTAGRAM_ID')
ig_pw = os.getenv('INSTAGRAM_PW')

cl = Client()
cl.login(ig_id, ig_pw)
print(f'로그인이 완료되었습니다. \n로그인된 계정: {ig_id}')

# 인스타그램 업로드를 위한 함수
def instagram_upload(today):
    photo_path = 'summary.jpeg'
    photo_path = Path(photo_path)
    print(f'{photo_path} 파일을 업로드합니다.')
    cl.photo_upload(photo_path, f'{today}의 구미중학교 급식 \n made by @d2.1ek')
    print('업로드를 완료했습니다.')

# 메인 프로세스
def process():
    today = datetime.date.today().strftime('%m월 %d일')
    print('메인 프로세스를 시작합니다.')
    print('급식 정보를 불러옵니다.')
    today_meal = meal_loader()
    print(today_meal)
    print('급식 정보를 성공적으로 불러왔습니다.')
    print('이미지를 생성합니다.')
    create_image_with_template(today_meal, today)
    print('이미지 생성이 완료되었습니다.')
    # instagram_upload(today)
    os.remove('summary.jpeg')
    print('업로드가 완료되었기 때문에 파일을 삭제합니다.')

# 자동 실행 코드
schedule.every().day.at("07:30").do(process)

while True:
    try:
        schedule.run_pending()
    except:
        pass
    time.sleep(60)
