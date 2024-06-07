# chat-gpt 연동

from dotenv import load_dotenv
import os
import openai

# API 키 불러오기
from openai import OpenAI
openai.api_key = "OpenAI_api_키"

client = OpenAI(api_key=openai.api_key)

# 이미지 URL
# image_url = f"https://raw.githubusercontent.com/{repo}/main/{path_in_repo}"
image_url = github_url

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "사진에는 필통, 모자, 충전기가 있어. 각각의 색, 재질, 대분류, 텍스트, 브랜드 로고를 한 단어씩 뽑아서 배열의 형태로 답변해줘"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                },
            ],
        }
    ],
    model="gpt-4o"
)

print(chat_completion.choices[0].message.content)