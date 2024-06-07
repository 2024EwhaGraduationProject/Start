import requests
from google.cloud import vision
from IPython.display import display, HTML
import base64

# 이미지 URL
file_name = github_url

# 이미지 다운로드
response = requests.get(file_name)
content = response.content

# Google Cloud Vision API 사용
image = vision.Image(content=content)

# client 초기화
client = vision.ImageAnnotatorClient()

# 로고 감지
response = client.logo_detection(image=image)
logos = response.logo_annotations

# 이미지 content를 base64로 변환하여 HTML로 표시
encoded_image = base64.b64encode(content).decode('utf-8')
image_html = f'<img src="data:image/jpeg;base64,{encoded_image}" width="300"/>'

# 이미지 및 결과를 표시하기 위해 HTML 콘텐츠 생성
html_content = f"""
<table style="width:100%">
  <tr>
    <td style="vertical-align: top; width: 50%;">
      {image_html}
    </td>
    <td style="vertical-align: top; width: 50%;">
      <ul>
"""

for logo in logos:
    html_content += f"<p>{logo.description}</p>"

html_content += """
      </ul>
    </td>
  </tr>
</table>
"""

# 결과 보여주기
display(HTML(html_content))