from gensim.models import Word2Vec

#prompt = "나이키 모자가 없어졌어. 색깔은 검정색이야"
prompt = "나이키 블랙 모자를 잃어버렸어"
print("prompt :",prompt)
items = word_dic

# 항목 리스트를 문자열로 변환
item_descriptions = [" ".join(item) for item in items]

# 사전 학습된 모델을 사용하는 것이 좋긴 한데 일단 임시로
sentences = [prompt.split()] + [item.split() for item in item_descriptions]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 주어진 문장의 벡터를 계산
def sentence_vector(sentence, model):
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if not word_vectors:
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)

# 주어진 문장의 벡터
prompt_vector = sentence_vector(prompt, model)

# 항목들의 벡터
item_vectors = [sentence_vector(item, model) for item in item_descriptions]

# 코사인 유사도 계산
def cosine_similarity(v1, v2):
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 각 항목과의 유사도 계산
similarities = [cosine_similarity(prompt_vector, item_vector) for item_vector in item_vectors]

# 각 항목과의 유사도 출력
for index, similarity in enumerate(similarities):
    print(f"항목 {index + 1} ({item_descriptions[index]})와의 유사도: {similarity:.4f}")

# 가장 유사한 항목 찾기
most_similar_index = np.argmax(similarities)
print(f"\n가장 유사한 항목: 항목 {most_similar_index + 1} ({item_descriptions[most_similar_index]})")