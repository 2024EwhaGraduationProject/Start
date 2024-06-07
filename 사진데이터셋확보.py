## 사진 데이터셋 확보
import pandas as pd
import numpy as np

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import random
random.seed(1886)

# 구글 드라이브 연동
from google.colab import drive
drive.mount('/content/drive')
data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0603.csv')
data.head()
object_num=data['object_num']
object_list=data['object_list']

#We have a pencil case, a hat, and a charger in this picture. Get the color, label, text, logo information of each item in array code format
print('%s 이렇게 총 %d개의 물건의 이미지야. 각 물건들의 색깔, 재질, 텍스트, 로고를 한 단어씩으로 나타내줄래? 오직 배열 형식으로만 답을 줘야해.' % (object_list[0],object_num[0]))