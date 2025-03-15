# image_generator.py
# 이미지를 생성하는 코드입니다.

from PIL import Image, ImageDraw, ImageFont

def create_image_with_template(text, date):
    # 날짜 정보 포맷팅

    # 제목에 날짜 추가
    full_title = f"오늘의 급식 - {date}"

    # 이미지 설정
    text_color = (0, 0, 0)
    title_color = (0, 0, 0)
    font_path = "./WantedSans-SemiBold.ttf"  # 한글 폰트 경로를 설정하세요
    font_size = 80  # 본문 크기를 15% 증가
    title_font_size = 75  # 제목 폰트 크기 감소
    background = './background.png'

    # 템플릿 이미지 불러오기
    template = Image.open(background).convert("RGB")
    width, height = template.size
    image = template.copy()
    draw = ImageDraw.Draw(image)

    # 폰트 설정
    font = ImageFont.truetype(font_path, font_size)
    title_font = ImageFont.truetype(font_path, title_font_size)

    # 제목 그리기
    title_bbox = draw.textbbox((0, 0), full_title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    draw.text(((width - title_width) / 2, 10), full_title, fill=title_color, font=title_font)  # 제목 위치를 더 위로 조정

    # 내용 그리기
    max_content_height = height - title_height - 60  # 제목 아래 여백을 고려한 최대 높이
    content_lines = text.split('\n')
    total_text_height = len(content_lines) * (font_size + 10)

    # 중앙 정렬을 위한 시작 y 위치 계산
    y_text = (height - total_text_height) / 2 + title_height / 2

    for line in content_lines:
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_width = line_bbox[2] - line_bbox[0]
        draw.text(((width - line_width) / 2, y_text), line, fill=text_color, font=font)
        y_text += font_size + 10


    # 이미지 저장 (PNG 형식)
    image.save(f'./summary.jpeg', format='JPEG')
