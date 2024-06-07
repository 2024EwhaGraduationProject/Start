!pip install google-cloud-vision

import os
from google.cloud import vision

# Set the environment variable for the credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/visionapi-trial-jsonkey.json'

# Initialize the Vision client
client = vision.ImageAnnotatorClient()