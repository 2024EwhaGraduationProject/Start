from time import time

#image_path = "/content/44.jpg"
image_path = github_url

prompt = "In this picture there is a pencil case, a hat, and a charger. The category, text, logo, and color for each item are distinguished one by one and output in the form of an array."

time_start = time()
image, output = caption_image(image_path, prompt)
time_end = time()

print("파일명:"+image_path+"\n")
print("본문: "+output+"\n")
print(f"소요시간: {time_end-time_start:.2f}s")