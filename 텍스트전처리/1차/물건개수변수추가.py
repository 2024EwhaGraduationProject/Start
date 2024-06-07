#물건 개수
object=[]
for i in range(len(lost_item)):
  object_num=int(re.findall("\d+\.+",object_list_remove[i])[-1].replace(".",""))
  object.append(object_num)
  #lost_item['object_num'][idx[i]]=object_num

data['object_num']= 0

for i in range(len(object)):
  data['object_num'][idx[i]]=object[i]

sum(data['object_num'][idx]==object)

data['object_num']

data.to_csv(base_url+'bunsilmul_0521.csv', index=False,encoding="utf-8-sig")