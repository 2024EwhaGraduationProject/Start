data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0531.csv')
data.tail(30)

for i in range(len(data)):
  if(data['section'][i]!="학생처습득"): data['object_num'][i]=1

data['object_num'].unique()

data['detail']=['']*len(data)

for i in range(len(data)):
  n=data['object_num'][i]
  data['detail'][i]=[['' for col in range(1)] for row in range(n)]

pattern = re.compile(r'(\d+)\.[^()]*\(([^)]+)\)')
lost_item=data[data['section']=="학생처습득"]
d=[['' for col in range(1)] for row in range(len(lost_item))]

for i in range(len(lost_item)):
  x=data['text'][idx[i]]
  x=x.split("오늘의 습득물입니다.")[1].split("학생서비스센터")[0].split("\n\n")
  #print(x)

  for j in x:
    matches = pattern.findall(j)
    if(matches != []):
      d[i] += matches

for i in range(len(lost_item)):
  d[i]=d[i][1:]

d[0:5]
z=data['detail'].copy()
idx=lost_item.index

for i in range(len(d)):
  n=len(d[i])

  for j in range(n):
    index=int(d[i][j][0])-1
    z[idx[i]][index].append(d[i][j][1])

data[['text','detail']][1:20]

data.to_csv(base_url+'bunsilmul_0602.csv', index=False,encoding="utf-8-sig")

data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0602.csv')

import ast
for i in range(len(data)):
  data['detail'][i]=data['detail'][i].replace("'',","")
  data['detail'][i]=ast.literal_eval(data['detail'][i])

data.to_csv(base_url+'bunsilmul_0603.csv', index=False,encoding="utf-8-sig")

data.to_csv(base_url+'bunsilmul_0603.csv', index=False,encoding="utf-8-sig")