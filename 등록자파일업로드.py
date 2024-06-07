# 드라이브에 파일 업로드
from google.colab import files

uploaded = files.upload()

# 업로드된 파일 확인
from google.colab import files
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# 파일 이름 업로드
for filename in uploaded.keys():
    print(f'업로드된 파일: {filename}')

    # opencv로 변경
    file_bytes = np.frombuffer(uploaded[filename], dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # BGR 이미지 (OpenCV 디폴트) --> 변환 RGB (Matplotlib)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Matplotlib 이용해서 이미지 보이기
    plt.imshow(image_rgb)
    plt.axis('off')  # Hide axes
    plt.show()

# 구글 드라이브 공유폴더에 업로드
import shutil

# src, dst 경로 설정
source_path = '/content/44.jpg'  # 초기 경로
destination_path = '/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/find.jpg' # 최종 경로

# 파일경로 이동
shutil.move(source_path, destination_path)

!pip install requests

# 깃허브에 자동 업로드
import shutil
import requests
import base64
import os

# 깃허브 업로드 함수
def upload_to_github(file_path, repo, path_in_repo, token):
    with open(file_path, 'rb') as file:
        content = file.read()

    base64_content = base64.b64encode(content).decode('utf-8')

    url = f"https://api.github.com/repos/{repo}/contents/{path_in_repo}"

    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    data = {
        "message": "Add image",
        "content": base64_content
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print("파일이 성공적으로 업로드 되었습니다. ")
    else:
        print(f"파일 업로드 실패: {response.status_code}")
        print(response.json())

# 깃허브 정보
repo = "깃허브_레포지토리_이름"
token = "깃허브_토큰"

# file_path에는 코랩에 있는 경로 저장
file_path = destination_path

# 깃허브에 업로드할 함수 실행
path_in_repo = "image/data_find/demo_record.jpg"  # 깃허브 image/data_find 뒤에 붙을 이름
upload_to_github(file_path, repo, path_in_repo, token)

# 이미지의 http 경로
print(f"https://raw.githubusercontent.com/{repo}/main/{path_in_repo}")

github_url = f"https://raw.githubusercontent.com/{repo}/main/{path_in_repo}"