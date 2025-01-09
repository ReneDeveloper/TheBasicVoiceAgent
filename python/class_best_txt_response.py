import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.cluster import KMeansClusterer, euclidean_distance
import string

#nltk.download('stopwords')
#nltk.download('punkt')

# Función para leer un archivo de texto plano
def read_text_file(file_name):
    with open(file_name, "r",encoding='utf-8') as file:
        return file.read()

# Leer un archivo de texto plano
txt_origen = read_text_file("../txt_food/origen.txt")

# Tokenizar el texto en palabras y eliminar las stopwords
stopwords_es = set(nltk.corpus.stopwords.words("spanish"))
tokens = [word.lower() for word in word_tokenize(txt_origen) if word.isalpha()]
tokens = [word for word in tokens if word not in stopwords_es and word not in list(string.punctuation)]

# Crear un objeto de texto
text = Text(tokens)

# Preguntar al usuario por una pregunta
question = "cuantas invasiones hubo a polonia"

# Encontrar las palabras más frecuentes en el texto
fdist = FreqDist(text)
most_common_words = [word[0] for word in fdist.most_common(100)]

# Crear un modelo de agrupamiento basado en K-means
kmeans = KMeansClusterer(5, euclidean_distance)
print("most_common_words:" + str(most_common_words))
clusters = kmeans.cluster(list(map(lambda x: [x], most_common_words)), assign_clusters=True)


clusters = kmeans.cluster(list(map(lambda x: [x], most_common_words)), assign_clusters=True)


# Encontrar las oraciones más relevantes para la pregunta
relevant_sentences = []
for sentence in sent_tokenize(txt_origen):
    for word in word_tokenize(sentence):
        if word in most_common_words:
            relevant_sentences.append(sentence)
            break

# Calificar cada oración relevante y seleccionar las 5 mejores
scores = {}
for sentence in relevant_sentences:
    score = 0
    for word in word_tokenize(sentence):
        if word in most_common_words:
            score += fdist.freq(word)
    scores[sentence] = score

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
best_sentences = [sentence[0] for sentence in sorted_scores[:5]]

# Imprimir las 5 mejores oraciones con sus factores

# Imprimir las 5 mejores oraciones con sus factores
for i, sentence in enumerate(best_sentences):
    score = sorted_scores[i][1]
    print(f"Respuesta {i + 1}: {sentence} (Factor: {score:.2f})")
