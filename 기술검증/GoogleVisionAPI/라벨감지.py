import requests
from google.cloud import vision
from IPython.display import display, HTML
import base64

# 이미지 url
file_name = github_url

# 이미지 다운로드
response = requests.get(file_name)
content = response.content

# Google Cloud Vision API 사용
image = vision.Image(content=content)

# client 초기화
client = vision.ImageAnnotatorClient()

# 라벨 감지
response = client.label_detection(image=image)
labels = response.label_annotations

# Convert image content to base64 for HTML display
encoded_image = base64.b64encode(content).decode('utf-8')
image_html = f'<img src="data:image/jpeg;base64,{encoded_image}" width="300"/>'

# Create HTML content to display the image and results
html_content = f"""
<table style="width:100%">
  <tr>
    <td style="vertical-align: top; width: 50%;">
      {image_html}
    </td>
    <td style="vertical-align: top; width: 50%;">
      <ul>
"""

for label in labels:
    html_content += f"<p>{label.description} (스코어: {label.score:.2f})</p>"

html_content += """
      </ul>
    </td>
  </tr>
</table>
"""

# 결과 보여주기
display(HTML(html_content))