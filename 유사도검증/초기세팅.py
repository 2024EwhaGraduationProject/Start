data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/졸업프로젝트/bunsilmul_0603.csv')

test_data=data.iloc[43]
test_data

test_data[['object_list','detail']]

import ast
test_data['detail']=ast.literal_eval(test_data['detail'])
gpt_result = ast.literal_eval(gpt_result)
gpt_result

# 검색을 위한 키워드 데이터셋 생성
word_dic=gpt_result.copy()
for i in range(test_data['object_num']):
  word_dic[i]+= test_data['detail'][i]
word_dic