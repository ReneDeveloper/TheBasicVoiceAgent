#food_stepwords_ES.py

import nltk
from nltk.corpus import stopwords

# Descargar el corpus de stopwords en español
nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')

# Imprimir algunas stopwords en español
print("Palabras vacías en español:", spanish_stopwords[:10])

print("Palabras vacías en español:", spanish_stopwords[:10])

for x in spanish_stopwords:
	print('x:' + x)




#otras_palabras = ["amor", "romance", "corazón", "beso", "abrazo", "pasión", "ternura", "cariño", "deseo", "compromiso", "felicidad", "suspiro", "enamorado", "flores", "compañía", "ilusión"]
otras_palabras_guerra = ["guerra", "batalla", "conflicto", "ejército", "violencia", "combate", "soldado", "arma", "destrucción", "ataque", "defensa", "lucha", "estrategia", "tensión", "caos", "conquista"]


import nltk
from nltk.corpus import stopwords
import random

# Descargar el corpus de stopwords en español
nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')

# Algunas palabras adicionales para la generación de frases
otras_palabras = ["sol", "luna", "mar", "montaña", "ciudad", "viaje", "aventura", "alegría", "amor"]

# Filtrar stopwords del conjunto de palabras adicionales
palabras_disponibles = [palabra for palabra in otras_palabras if palabra not in spanish_stopwords]

# Generar una frase aleatoria
if palabras_disponibles:
    sujeto = random.choice(palabras_disponibles)
    verbo = random.choice(["es", "fue", "será", "está"])
    objeto = random.choice(palabras_disponibles)

    frase_aleatoria = f"{sujeto} {verbo} {objeto}."
    print(frase_aleatoria)
else:
    print("No hay palabras disponibles para construir una frase.")
