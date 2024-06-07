import urllib.request
import time

img_dst=r"C:\Users\seoyounglee\workspace\졸프\image/" #각자 경로 적고 image라는 폴더를 만들면 거기에 저장됨
for i in range(len(data)):
    url=data['image'][i]
    if(url != "no image"): urllib.request.urlretrieve(url, img_dst+str(i+1)+'.jpg')
    #img = Image.open(name)