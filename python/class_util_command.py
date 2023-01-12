import re
import json
import zipfile
import os

from nltk.corpus import stopwords

class UtilCommand:

    __LOG_ACTIVO = True
    #__src_comandos = None
    __COMANDOS = None
    __RESPONSES = None

#    _MAP_SUCURSALES_POSIBLES = {"local lyon":1,"enjoy coquimbo":1,"coquimbo":1, "viña":2,"viña del mar":2, "enjoy viña":2,  "enjoy santiago":3 ,"enjoy de los andes":3,"enjoy chiloe":4 }
#    __MAPA_BASE = None
#    def __init__(self,mapa_base):

    def __init__(self, file_tag):
        """function """
        self.log("FLUJO:UtilCommand:__init__:file_tag" + file_tag)
        self.carga_comandos(file_tag)

    def log(self,msg_):
        """function """
        if self.__LOG_ACTIVO:
            print("LOG:UtilCommand:" + msg_)

    def batch(self,src_,__MAPA_BASE):
        """function """
        batch_out = ""
        self.log(  "Entrando a modo batch:  "   )
        
        txtRaw = ""
        try:
            f=open(src_,'r',errors = 'ignore')
            txtRaw=f.read()
            txtRaw=txtRaw.lower()# minúsculas
        finally:
            f.close()

        for mensajeHumano in iter(txtRaw.splitlines()):

            if (mensajeHumano==""):continue
            if (mensajeHumano[0:1]=="#"):continue
            #mensajeHumano = self.string_FIX_002(mensajeHumano)
            print("------------------------------------------------------------------------------------------------------------------")
            print("MENSAJE HUMANO:'" + mensajeHumano+"'")
            print("------------------------------------------------------------------------------------------------------------------")
            #mensajeHumano = self.util.string_FIX_002(mensajeHumano)

            mapaComando = self.getMapaComando(mensajeHumano,__MAPA_BASE)

            print(  "MAPA_MENSAJE:" + str(mapaComando)  )
            print("------------------------------------------------------------------------------------------------------------------")

        return batch_out

    def getMapaComando(self,txt_entrada):
        """function """
        #print("getMapaComando:" + "status de [self.__COMANDOS]:" + str(self.__COMANDOS) )
        #if (self.__COMANDOS==None):
        #    print("getMapaComando:status: self.__src_Comandos: " + str(self.__src_Comandos) )
        #    self.cargaComandos(self.__src_Comandos)
        salida_=""

        txt = txt_entrada.lower()
        txt = txt.replace("á","a")
        txt = txt.replace("é","e")
        txt = txt.replace("í","i")
        txt = txt.replace("ó","o")
        txt = txt.replace("ú","u")

        txt_post = "" + txt

        salida_DICT = {}
        salida_DICT["txt_entrada"]=txt_entrada

        #ITERAR LAS PALABRAS DE LA LISTA DE COMANDOS
        #GENERAR_BOOLEAN = SI EL TEXTO DEL ARREGLO DEL COMANDO, SE ENCUENTRA EN LA FRASE HUMANA

        for key_comando in self.__COMANDOS.keys():
            #print ("------------------------------------------")
            #print ("key_comando:" + key_comando)
            #print ( "posibles frases:" + str(self.__COMANDOS.get(key_comando)) )
            if key_comando[0:4]=="key_":
                #print("es una key de comando")
                tieneComando = any(string in txt_entrada for string in self.__COMANDOS.get(key_comando) )
                #print ( "tieneComando:" + str(tieneComando) )
                if tieneComando:
                    salida_DICT[ key_comando ] = tieneComando

            #lo mismo para la key, pero parametros podría ser otro vector de salida
            #configurable a partir de un segundo comando
            if key_comando[0:4]=="par_": 
                #print("es un parámetro para la key: " + key_comando)
                a9999 = 0
                #tieneComando = any(string in txt_entrada for string in str(self.__COMANDOS.get(key_comando)) )
            #print ("------------------------------------------")
        return salida_DICT

    def txt_open_FIX_RAW(self,scr_):
        """function """
        f=open(scr_,'r',errors = 'ignore')
        raw=f.read()
        raw=raw.lower()# converts to lowercase
        raw_fix = "" + raw
        raw_fix = self.string_FIX_002(raw_fix)
        return raw_fix

    def carga_comandos(self,file_tag):
        """function """
        src_comandos = f'commands/COMMAND_DEF_{file_tag}.json'

        print("carga comandos:" + str(src_comandos) )
        salida_ = ""
        if (self.__COMANDOS==None):
            f = open(src_comandos, 'r')
            self.__COMANDOS = json.loads(f.read())
            print("CARGANDO:archivoComandos:" + str(src_comandos) )
            print("CARGANDO:archivoComandos:" + str(self.__COMANDOS) )
            salida_ = "ok comandos"

        src_response = f'commands/COMMAND_DEF_{file_tag}_RESPONSES.json'
        print("carga response:" + src_response )

        if (self.__RESPONSES==None):
            f = open(src_response, 'r')
            self.__RESPONSES = json.loads(f.read())
            print("CARGANDO:archivoResponses:" + str(src_response) )
            print("CARGANDO:archivoResponses:" + str(self.__RESPONSES) )
            salida_ = salida_ + " ok responses"

        return salida_

    def string_remove_stop_words(self,val):
        """function """
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
