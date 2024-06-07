from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 주어진 문장과 항목 리스트
#prompt = "분홍색 토끼 모양의 필통을 잃어버렸어."
prompt = "나이키 모자가 없어졌어. 색깔은 검정색이야"
items = word_dic

# 항목 리스트를 문자열로 변환
item_descriptions = [" ".join(item) for item in items]

# 유사도 계산을 위해 주어진 문장을 리스트에 추가
documents = item_descriptions + [prompt]

# TF-IDF 벡터라이저를 사용하여 문서들을 벡터화
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(), lowercase=False,token_pattern=None).fit_transform(documents)
vectors = vectorizer.toarray()

# 마지막 벡터(주어진 문장)와 다른 벡터(항목들) 간의 코사인 유사도를 계산
cosine_similarities = cosine_similarity(vectors[-1:], vectors[:-1]).flatten()

# 각 항목과의 유사도 출력
for index, similarity in enumerate(cosine_similarities):
    print(f"항목 {index + 1} ({item_descriptions[index]})와의 유사도: {similarity:.4f}")

# 가장 유사한 항목 찾기
most_similar_index = cosine_similarities.argmax()
print(f"\n가장 유사한 항목: 항목 {most_similar_index + 1} ({item_descriptions[most_similar_index]})")