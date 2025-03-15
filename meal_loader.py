# meal_loader.py
# 급식 정보를 가져오는 모듈입니다.

from dotenv import load_dotenv
import os
import datetime
import requests
import json

# API 키 설정
load_dotenv()
NEIS_APIKEY = os.getenv("NEIS_APIKEY")


# 급식 정보 가져오는 함수
def meal_loader():
    # 변수 설정
    today = datetime.date.today().strftime('%y%m%d')
    api_url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'  # mealServiceDietInfo = NEIS API의 급식정보 API
    office_code = 'R10'  # R10 = 경상북도교육청의 시도교육청 코드
    school_code = '8801139'  # 8801139 = 구미중학교(경상북도)의 행정표준코드
    params = {
        'KEY': NEIS_APIKEY,
        'TYPE': 'json',
        'pIndex': 1,
        'pSize': 1,
        'ATPT_OFCDC_SC_CODE': office_code,
        'SD_SCHUL_CODE': school_code,
        'MLSV_YMD': today  # YYYYMMDD 형식으로 작성할 것.
    }

    # thanks for hminkoo10(https://github.com/hminkoo10/solvit_lunch/blob/main/main.py line#102)
    response = requests.get(api_url, params=params, json=True)
    response.encoding = 'UTF-8'
    data = response.json()
    return data["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].replace("<br/>", "\n")
