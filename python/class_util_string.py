
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
		val_fix=""+val

		val_fix = val_fix.replace("ãƒâ¡", "á")
		val_fix = val_fix.replace("ãƒâ³", "ó")
		val_fix = val_fix.replace("ãƒâ±", "ñ")

		val_fix = val_fix.replace("ãƒâ©", "é")
		val_fix = val_fix.replace("ã©", "é")
		
		val_fix = val_fix.replace("ãƒâº", "ú")

		val_fix = val_fix.replace("ã¢â€âœ", "\"")
		val_fix = val_fix.replace("ã¢â€â", "\"")
		val_fix = val_fix.replace("ã‚â´", "'")
		val_fix = val_fix.replace("ãƒâ­", "í")


		val_fix = val_fix.replace("ecommerce", "e-commerce")
		val_fix = val_fix.replace("crossborder", "cross-border")
		val_fix = val_fix.replace("ehunting", "e-hunting")

		val_fix = val_fix.replace("\na-\n", "\n")
		val_fix = val_fix.replace("\na+\n", "\n")
		val_fix = val_fix.replace("\n\n", "\n")
		val_fix = val_fix.replace("\n\n", "\n")
		val_fix = val_fix.replace("\n\n", "\n")
		val_fix = val_fix.replace("\n\n", "\n")

		return val_fix

	def string_FIX_001(self,val):
		val_fix=""+val
		val_fix = val_fix.replace("ãƒâ¡", "á")
		val_fix = val_fix.replace("ãƒâ³", "ó")
		val_fix = val_fix.replace("ãƒâ±", "ñ")
		val_fix = val_fix.replace("ãƒâ©", "é")
		val_fix = val_fix.replace("ãƒâº", "ú")
		val_fix = val_fix.replace("ã¢â€âœ", "\"")
		val_fix = val_fix.replace("ã¢â€â", "\"")
		val_fix = val_fix.replace("ã‚â´", "'")
		val_fix = val_fix.replace("ãƒâ­", "í")
		return val_fix

	def string_FIX_002(self,val):
		val_fix=""+val
		val_fix = val_fix.replace("ã¡", "á")
		val_fix = val_fix.replace("ã³", "ó")
		val_fix = val_fix.replace("ã±", "ñ")
		val_fix = val_fix.replace("ã©", "é")
		val_fix = val_fix.replace("ãº", "ú")
		val_fix = val_fix.replace("â€œ", "\"")
		val_fix = val_fix.replace("â€", "\"")
		#val_fix = val_fix.replace("ã‚â´", "'")
		val_fix = val_fix.replace("ã­", "í")
		return val_fix

	def string_remove_stop_words(self,val):
		val_clean = ""
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
				val_clean = val_clean + ' ' + word

		#print (important_words)

		#This is the more pythonic way
		#important_words = filter(lambda x: x not in stopwords.words('spanish'), words)

		#print (important_words )
		val_clean = val_clean.strip()
		return val_clean

	def buscaComando(self,val):
		salida_omando = "sin_comando"
		val_clean = self.string_remove_stop_words(val)
		print("buscando comando en: -->" + val_clean + "<--")
		if "cuéntame" in val_clean or "sabes" in val_clean or "dime" in val_clean or "información" in val_clean:
			val_clean = val_clean.replace("acerca","")
			val_clean = val_clean.replace("cuéntame","sabes")
			val_clean = val_clean.replace("dime","sabes")
			val_clean = val_clean.replace("sabes","")
			val_clean = val_clean.strip()
			predicado = val_clean
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "sabes" + "__" + predicado

		if "nombre" in val_clean or ( "mi nombre es " in val or "me llamo " in val):
			#predicado = val_clean[val_clean.find("nombre"):len(val_clean)] 
			val_clean = val_clean.replace("nombre","")
			val_clean = val_clean.replace("llamo","")
			val_clean = val_clean.strip()
			predicado = val_clean
			salida_omando = "nombre" + "__" + predicado

		if "hasta luego" in val or "adios" in val_clean or "nos vemos" in val or "chao" in val_clean:
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "despedida" + "__" + "despedida"

		if "chetumare" in val_clean or "imbécil" in val_clean:
			predicado = "<nombre>"
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "insultar" + "__" + "<nombre>"

		if "maldito" in val_clean or "escoria" in val_clean:
			predicado = "<nombre>"
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "insultar2" + "__" + "<nombre>"

		if "hola" in val_clean :
			predicado = "<nombre>"
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "saluda" + "__" + "<nombre>"

		bol_contexto_locales =  any(string in val_clean for string in ["cargar contexto locales","carga contexto locales","cambiar contexto locales","entrar a contexto locales"] )

		if bol_contexto_locales:
			#predicado = "<nombre>"
			#predicado = val_clean[val_clean.find("sabes"):len(val_clean)] 
			salida_omando = "carga_contexto" + "__" + "locales"

		salida_omando = salida_omando.replace("  "," ")
		if salida_omando!="sin_comando":
			print("comando encontrado:" + salida_omando)

		return salida_omando

#salida = "que sabes acerca de"

#util = UtilString()
#print(util.buscaComando(salida))


