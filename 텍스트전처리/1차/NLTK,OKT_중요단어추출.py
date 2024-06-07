import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.tag import pos_tag


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

#object_list_remove
for i in range(len(object_list_remove)):
  object_list_remove[i]=re.sub(r'\d', '', object_list_remove[i]).replace(".","")

pos_tag(word_tokenize(object_list_remove[0]))
word_tokenize(object_list_remove[0])

word_dic=[]
for i in range(len(object_list_remove)):
  word_dic.append(pos_tag(word_tokenize(object_list_remove[i])))

word_dic[0:6]

!pip install konlpy
from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

okt.pos(object_list_remove[0])
okt.nouns(object_list[0]) #명사만 추출

kkma.pos(object_list_remove[0])