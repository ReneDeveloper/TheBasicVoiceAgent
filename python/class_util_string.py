
import re
from nltk.corpus import stopwords

class UtilString:

	def __init__(self):

		print("UtilString")


	def txt_open_FIX_RAW(self,scr_):

		f=open(scr_,'r',errors = 'ignore')
		raw=f.read()
		raw=raw.lower()# converts to lowercase
		raw_fix = "" + raw
		raw_fix = self.string_FIX_002(raw_fix)
		return raw_fix

	def txt_DATAFIX_HTML_REPLACE(self,txt2clean):
		out_txt_DATAFIX_HTML_REPLACE=""+txt2clean

		if (self._DATAFIX_HTML_REPLACE==None):
			f = open('DATAFIX_HTML_REPLACE_ISO.txt', 'r')
			self._DATAFIX_HTML_REPLACE = json.loads(f.read())
			print("CARGANDO:DATAFIX_HTML_REPLACE:" + str(self._DATAFIX_HTML_REPLACE) )
		s = txt2clean
		d = self._DATAFIX_HTML_REPLACE
		#pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
		pattern = re.compile('|'.join(d.keys()))
		result = pattern.sub(lambda x: d[x.group()], s)

		out_txt_DATAFIX_HTML_REPLACE = result
		print ("asi queda: " + result)

		return out_txt_DATAFIX_HTML_REPLACE



	def string_FIX_000(self,val):
		valFix=""+val

		valFix = valFix.replace("ãƒâ¡", "á")
		valFix = valFix.replace("ãƒâ³", "ó")
		valFix = valFix.replace("ãƒâ±", "ñ")

		valFix = valFix.replace("ãƒâ©", "é")
		valFix = valFix.replace("ã©", "é")
		
		valFix = valFix.replace("ãƒâº", "ú")

		valFix = valFix.replace("ã¢â€âœ", "\"")
		valFix = valFix.replace("ã¢â€â", "\"")
		valFix = valFix.replace("ã‚â´", "'")
		valFix = valFix.replace("ãƒâ­", "í")


		valFix = valFix.replace("ecommerce", "e-commerce")
		valFix = valFix.replace("crossborder", "cross-border")
		valFix = valFix.replace("ehunting", "e-hunting")

		valFix = valFix.replace("\na-\n", "\n")
		valFix = valFix.replace("\na+\n", "\n")
		valFix = valFix.replace("\n\n", "\n")
		valFix = valFix.replace("\n\n", "\n")
		valFix = valFix.replace("\n\n", "\n")
		valFix = valFix.replace("\n\n", "\n")

		return valFix

	def string_FIX_001(self,val):
		valFix=""+val
		valFix = valFix.replace("ãƒâ¡", "á")
		valFix = valFix.replace("ãƒâ³", "ó")
		valFix = valFix.replace("ãƒâ±", "ñ")
		valFix = valFix.replace("ãƒâ©", "é")
		valFix = valFix.replace("ãƒâº", "ú")
		valFix = valFix.replace("ã¢â€âœ", "\"")
		valFix = valFix.replace("ã¢â€â", "\"")
		valFix = valFix.replace("ã‚â´", "'")
		valFix = valFix.replace("ãƒâ­", "í")
		return valFix

	def string_FIX_002(self,val):
		valFix=""+val
		valFix = valFix.replace("ã¡", "á")
		valFix = valFix.replace("ã³", "ó")
		valFix = valFix.replace("ã±", "ñ")
		valFix = valFix.replace("ã©", "é")
		valFix = valFix.replace("ãº", "ú")
		valFix = valFix.replace("â€œ", "\"")
		valFix = valFix.replace("â€", "\"")
		#valFix = valFix.replace("ã‚â´", "'")
		valFix = valFix.replace("ã­", "í")
		return valFix

	def string_remove_stop_words(self,val):
		valClean = ""
		#val = 'El problema del matrimonio es que se acaba todas las noches despues de hacer el amor, y hay que volver a reconstruirlo todas las mananas antes del desayuno.'

		#We only want to work with lowercase for the comparisons
		val = val.lower() 

		#remove punctuation and split into seperate words
		#words = re.findall(r'\w+', scentence,flags = re.UNICODE | re.LOCALE) 
		words = re.findall(r'\w+', val,flags = re.UNICODE ) 

		#This is the simple way to remove stop words
		important_words=[]
		for word in words:
			if word not in stopwords.words('spanish'):
				important_words.append(word)
				valClean = valClean + ' ' + word

		#print (important_words)

		#This is the more pythonic way
		#important_words = filter(lambda x: x not in stopwords.words('spanish'), words)

		#print (important_words )
		valClean = valClean.strip()
		return valClean

	def buscaComando(self,val):
		salidaComando = "sin_comando"
		valClean = self.string_remove_stop_words(val)
		print("buscando comando en: -->" + valClean + "<--")
		if ("cuéntame" in valClean or "sabes" in valClean or "dime" in valClean or "información" in valClean):
			valClean = valClean.replace("acerca","")
			valClean = valClean.replace("cuéntame","sabes")
			valClean = valClean.replace("dime","sabes")
			valClean = valClean.replace("sabes","")
			valClean = valClean.strip()
			predicado = valClean
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "sabes" + "__" + predicado

		if ( ("nombre" in valClean ) or "mi nombre es " in val or "me llamo " in val):
			#predicado = valClean[valClean.find("nombre"):len(valClean)] 
			valClean = valClean.replace("nombre","")
			valClean = valClean.replace("llamo","")
			valClean = valClean.strip()
			predicado = valClean
			salidaComando = "nombre" + "__" + predicado

		if ("hasta luego" in val or "adios" in valClean or "nos vemos" in val or "chao" in valClean):
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "despedida" + "__" + "despedida"


		if ("chetumare" in valClean or "imbécil" in valClean):
			predicado = "<nombre>"
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "insultar" + "__" + "<nombre>"

		if ("maldito" in valClean or "escoria" in valClean):
			predicado = "<nombre>"
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "insultar2" + "__" + "<nombre>"

		if ("hola" in valClean ):
			predicado = "<nombre>"
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "saluda" + "__" + "<nombre>"

		bol_contexto_locales =  any(string in valClean for string in ["cargar contexto locales","carga contexto locales","cambiar contexto locales","entrar a contexto locales"] )

		if (bol_contexto_locales):
			#predicado = "<nombre>"
			#predicado = valClean[valClean.find("sabes"):len(valClean)] 
			salidaComando = "carga_contexto" + "__" + "locales"

		salidaComando = salidaComando.replace("  "," ")
		if (salidaComando!="sin_comando"):
			print("comando encontrado:" + salidaComando)

		return salidaComando

#salida = "que sabes acerca de"

#util = UtilString()
#print(util.buscaComando(salida))


