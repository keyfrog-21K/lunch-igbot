# lunch-igbot
- 급식 메뉴를 인스타그램 게시물을 통해 매일 오전 7시 30분에 업로드하는 봇입니다.

# 파일 구조
```
📁 lunch-igbot
L .env.example: .env 비밀 저장소의 예시 파일입니다. 실제 구동환경에서는 .env 파일로 대체하세요.
L .gitignore: gitignore 파일입니다. Python, macOS, PyCharm 환경에서 작성되었습니다.
L background.png: 배경 파일입니다. 아무 1:1 정사각형 비율의 파일로 대체하셔도 무방합니다.
L image_generator.py: 이미지를 생성하는 파일입니다. main.py에 모듈로 불러와서 사용합니다.
L main.py: 메인 구동 파일입니다. 인스타그램 게시 함수와 자동화 프로세스가 포함되어 있습니다.
L meal_loader.py: 급식 정보를 불러오는 파일입니다. 교육청, 학교코드는 적절히 수정하시면 됩니다.
L README.md: 여러분이 보고 계신 이 파일입니다.
L requirements.txt: 의존성 파일입니다. pip install -r requirements.txt 명령으로 설치하세요.
L WantedSans-SemiBold.ttf: image_generator.py를 위한 폰트 파일입니다. Wanted Sans SemiBold입니다.
```

# 구동 방식
1. 매일 오전 7시 30분에 메인 프로세스가 실행됩니다. 
2. 급식 정보를 불러옵니다. 
3. 불러온 정보를 기반으로 이미지 파일을 만듭니다.
4. 만들어진 이미지 파일을 인스타그램에 업로드합니다.