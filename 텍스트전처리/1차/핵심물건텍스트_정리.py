n=len(lost_item)
object_list=['']*n
idx=lost_item.index

for i in range(n):
  x=lost_item['text'][idx[i]]
  xx=x.split("오늘의 습득물입니다.")[1].split("학생서비스센터")[0].replace("\n"," ")
  object_list[i]=xx

pattern = r'\([^)]*\)'
n=len(object_list)

object_list_remove=object_list.copy()

for i in range(n):
  text = re.sub(pattern=pattern, repl='', string= object_list[i])
  object_list_remove[i]=text

object_list_remove[0:5]

x=pd.DataFrame({"object_text" : object_list_remove})
x.to_csv(base_url+'object_text.csv', index=False,encoding="utf-8-sig")

text_original=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/object_text.csv')
n=len(text_original);print(n)

text=text_original.copy()
item_list=[]

for i in range(n):
  text['object_text'][i]=re.sub(r"\s+", "", text['object_text'][i]) #불필요한 공백 제거
  text['object_text'][i]=re.sub(r'\d', '', text['object_text'][i]) #숫자제거
  text['object_text'][i]=text['object_text'][i].replace("."," ") #.제거
  text['object_text'][i]=text['object_text'][i].lower()
  item_list.append(text['object_text'][i])

item_list[0:5]
x=pd.DataFrame(item_list); print(len(x))
x.to_csv(base_url+'item_list_clean.csv', index=False,encoding="utf-8-sig")

data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0521.csv')

data['object_list']=['']*len(data)
data['detail']=['']*len(data)

for i in range(len(x)):
  data['object_list'][idx[i]]=item_list[i]

data.head()
data.to_csv(base_url+'bunsilmul_0531.csv', index=False,encoding="utf-8-sig")

data['object_list'][15:17]