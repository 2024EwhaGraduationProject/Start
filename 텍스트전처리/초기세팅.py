import cv2
import pandas as pd
import numpy as np
import nltk
import re

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

base_url='/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/'

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0517.csv')
data.head()

lost_item=data[data['section']=="학생처습득"]
n=len(lost_item)
idx=lost_item.index
idx