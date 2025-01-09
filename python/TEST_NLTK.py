import nltk
from nltk.tokenize import sent_tokenize
from nltk.metrics.distance import jaccard_distance
from collections import defaultdict

#read_text_file("../txt_food/origen.txt")

with open("../txt_food/origen.txt", "r",encoding='utf-8') as file:
    origen_txt = file.read()

sentences = sent_tokenize(origen_txt)

target_sentence = "La Comunidad Internacional"
similarity_scores = defaultdict(float)

for sent in sentences:
    similarity_scores[sent] = jaccard_distance(set(sent.split()), set(target_sentence.split()))

top_3_similar_sentences = sorted(similarity_scores, key=similarity_scores.get)[:3]

print("Top 3 similar sentences:")
for sent in top_3_similar_sentences:
    print(sent)








from googlesearch import search

def search_jokes(query):
    jokes = []
    for result in search(query + " chistes", num=10, stop=10, pause=2):
        if "chistes" in result and "jokes" in result:
            jokes.append(result)
    return jokes

user_query = input("Enter a search term: ")
jokes = search_jokes(user_query)

for joke in jokes:
    print(joke)