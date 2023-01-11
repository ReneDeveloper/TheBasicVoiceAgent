"""class_basic_voice_bot.py"""
import nltk #RSILVA_20200305 NATURAL LANGUAGE TOOL KIT
import speech_recognition as sr #RSILVA_20200305 RECONOCIMIENTO DE VOZ ENTRADA
import pyttsx3 #RSILVA_20200305 PYTHON SPEECH TEXT TO SPEECH

import requests
import random
from class_util_string import UtilString 
#from BASIC_BOT_TRADUCE_PERIODOS_20200210 import BasicTraductor_PERIODOS 

from class_util_command import UtilCommand
#from UTIL_RESPONSE_20200110 import UtilResponse

class BasicVoiceBot:

    __name              = 'Sin configurar Bot'
    __sex               = 'o' #a:mujer o:hombre
    __contexto          = 'sin contexto'
    __hablar            = True
    __humanBatchVoice   = True
    __nombre_conocido   = ''
    __maxspeed          = 0
    __log               = True

    __traductor_001       = None
    _DATAFIX_HTML_REPLACE = None

    _POSIBLE_SALUDO = ("Hola", "Hola, cómo has estado", "Hola, que bueno verte")#THIS IS LIKE THE LIST OF A DECISION IN SOME CASES
    _POSIBLE_DESPEDIDA = ("Hasta luego", "Adiosito", "Nos vemos", "Hasta pronto", "Adios")
    _POSIBLE_GO = ("dale", "ok", "correcto", "continua", "avanza")
    _POSIBLE_NO_ENTIENDO = ("no pude entenderte", "no sé a que te refieres", "creo que me falta contexto para entenderte", "no tengo información", "no tengo datos de eso", "no pude entenderte, me faltan datos", "te lo dije, me faltan datos", "quede plop", "me he quedado plop con esa pregunta")
    _POSIBLE_INSULTO = ("porque me insultas pelao colla", "no me insultes o los gatos y los patos dominaran el mundo", "no me insultes no sabes de lo que soy capaz", "quien te crees para insultarme tonto", "acabaré con el mundo maldito, te eliminaré, na mentira , era broma", "te güoi a matar te güoi a destruiiiiiii")
    _POSIBLE_INSULTO_MALDITO = ("hijo de la chingada", "no manches güey", "samba canuta")
    _POSIBLE_INSULTO_RECIBIDO = ("tonto", "gil", "malulo")
    _POSIBLE_INSULTO_3 = ("estúpido", "pajaron", "malulo", "que roteque")

    __util_String = None
    util_Command = None
    #__util_Command_SRC = None

    engine = None
    engine_batch = None

    __map_COMANDOS = None

    def __init__(self,name_, file_tag):
        """function ____"""
        #self.__init__(self)
        self.log('BasicVoiceBot:INIT:')
        self.__name = 'Sin configurar bot'
        self.util_String = UtilString()
        self.log('BasicVoiceBot:INIT:SETEANDO COMANDOS POR DEFECTO')
        self.util_Command = UtilCommand(f'commands/COMMAND_DEF_{file_tag}.json')

        self.__name = name_

        self.engine_batch = pyttsx3.init()
        #botConfig = ""
        self.engine = pyttsx3.init()


    def log(self,txtLog):
        """function ____"""
        if (self.__log):
            print(self.__name + ":" + str(txtLog))

    def saludo(self):
        """function ____"""
        msgSaludo = random.choice(self._POSIBLE_SALUDO)
        msgSaludo = msgSaludo + ', mi nombre es ' + self.__name + ': Pregúntame cosas.' 
        msgSaludo = msgSaludo + '. Para salir, dime Bye!.'

        msg_saludo_contextos = 'Estoy programad' + self.__sex + ' para aprendizaje automático y manejo de contextos' #los siguientes contextos: " + str(POSIBLES_CONTEXTOS)
        #msg_saludo_contextos = "Si no entiendo " +   str(POSIBLES_NO_ENTIENDO) 
        #print(msgSaludo)
        self.log('saludo: ' + msgSaludo)
        return msgSaludo
        
    def despedida(self):
        """function ____"""
        msgSaludo = random.choice(self._POSIBLE_DESPEDIDA)
        self.log('despedida: ' + msgSaludo)

    def load(self):
        self.log('*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*')
        self.log('*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*')

    #def txt_FIX_ISO(self,user_response):
    #    robo_response=""+user_response
    #    robo_response = robo_response.replace("\\xe2\\x80\\x9c", "\"")
    #    robo_response = robo_response.replace("brasil ", "brazil ")
    #    return robo_response

    #def getUtilComando(self):

        #self.log("getUtilComando-->self.__util_Command:" + self.__util_Command)
        #self.log("getUtilComando-->self.__util_Command_SRC:" + self.__util_Command_SRC)
        #self.log("getUtilComando-->self.__util_Command.__util_Command_SRC:" + self.__util_Command.__util_Command_SRC)

        #if (self.__util_Command==None):
        #    self.__util_Command = UtilCommand()
        #    self.__util_Command.__util_Command_SRC = self.__util_Command_SRC
        #    print("EMPEZANDO CARGA DE COMANDOS:" + self.__util_Command_SRC)
        #    self.__util_Command.cargaComandos(self.__util_Command_SRC)

        #self.log("getUtilComando:" + self.__util_Command.__util_Command_SRC)

        #return self.__util_Command

    def setUtilComando_SRC(self,src_comandos):
        print("setUtilComando_SRC: " + src_comandos)
        util_command = UtilCommand(src_comandos)
        #util_command.cargaComandos(src_comandos)
        self.__util_Command = util_command

        """
            def getUtilComando_SRC(self):
                if (self.__util_Command_SRC==None or self.__util_Command_SRC==""):
                    self.__util_Command_SRC = ""
                return self.__util_Command_SRC
        """


#    XXXXXXXX  XX    XX XXXXXXXX XXXXXXXX XXXXXXX   XXXXXX    XXXXXX XXXXXXXX
#       XX     XXX   XX    XX    XX       XX    XX XXX  XXX  X          XX   
#       XX     XXXX  XX    XX    XXXXXXXX XX    XX XX    XX X           XX   
#       XX     XX XX XX    XX    XX       XXXXXXX  XXXXXXXX X           XX   
#       XX     XX  XXXX    XX    XX       XX  XX   XX    XX X           XX   
#       XX     XX   XXX    XX    XX       XX   XX  XX    XX  X          XX   
#    XXXXXXXX  XX    XX    XX    XXXXXXXX XX    XX XX    XX   XXXXXX    XX   

    def interact(self,msg):

        interact_out = "No te entiendo, me falta información"

#        if (self.__util_Command==None):
#            self.__util_Command = UtilCommand("COMMAND_DEF_20200210.txt")
        mapa_COMANDO = self.util_Command.getMapaComando(msg)

        comando="sin_comando"#ignorando 

        self.log("mapa_COMANDO:" + str(mapa_COMANDO)  ) 

        if (comando=="saluda"):
            msgSaludo = ""

            if (self.__nombre_conocido!=""):
                msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + self.__nombre_conocido
            else:
                msgSaludo = random.choice(self._POSIBLE_SALUDO) + ", no sé como te llamas, por favor dime tu nombre."

            interact_comando_out = msgSaludo

        if ("key_basic_setnombre" in mapa_COMANDO.keys()):
            print("SETEANDO NOMBRE: " + msg)
            msgSaludo = ""
            predicado = "definicion de nombre"
            
            if ("juanito" in msg):
                predicado = "Juanito Pérez"
            #self.__nombre_conocido = predicado

            if ("pepe" in msg):
                predicado = "Pepe"
            #self.__nombre_conocido = predicado

            if ("rené" in msg):
                predicado = "René"
            #self.__nombre_conocido = predicado

            if (self.__nombre_conocido==""):
                self.__nombre_conocido = predicado
            else:
                self.__nombre_conocido = predicado

            msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + predicado  + ", he almacenado tu nombre"
            interact_out = msgSaludo

        if ("key_logistica_busqueda" in mapa_COMANDO.keys()):
            print("BUSCANDO PRODUCTO")
            #msgSaludo = ""
            interact_out = "producto no encontrado"

            if (msg=="dime donde estan los tubos de pvc"):
                predicado = "tubos de pvc"
                busquedaLogistica = "quedan 485 " + predicado + " en el pasillo 5, columna 5, estante C"
                interact_out = "producto encontrado: " + busquedaLogistica

            if (msg=="quedan tornillos roscalata"):
                predicado = "tornillos roscalata"
                busquedaLogistica = "quedan 5 cajas de " + predicado + " en el pasillo 1, columna 2, estante B"
                interact_out = "producto encontrado: " + busquedaLogistica


        if ("key_basic_ayuda" in mapa_COMANDO.keys()):
            interact_out = "por supuesto que puedo ayudarte, conexión a E R P realizada con éxito"

        if ("key_sabes_chistes" in mapa_COMANDO.keys()):
            interact_out = "por supuesto que sé contar chistes, dime el tema del chiste que quieres"

        if ("key_chiste_ciegos" in mapa_COMANDO.keys()):

            interact_out = "Van dos ciegos y le dice uno al otro:— Ojalá lloviera. y el otro contesta— Ojalá yo también., pues ostia chaval."

        if ("key_chiste_foca" in mapa_COMANDO.keys()):
            interact_out = "— ¿Qué le dijo una foca gringa su madre?, —AI loviu, mother foca. Ostia Joder, jo jo jo jo jo, ese chiste está muy bueno"

        if ("key_chiste_dj" in mapa_COMANDO.keys()):
            interact_out = "— ¿Sabes por qué no se puede discutir con un dj? — Pues que Porque siempre están cambiando de tema, jajaja ja ja ja jojojo ostias que me rio."

        if (comando=="getnombre"):
            msgSaludo = "mi nombre es " + self.__name #random.choice(self._POSIBLE_SALUDO) 
            return msgSaludo

        if (comando=="despedida"):
            msgAdios = ""

            if (self.__nombre_conocido!=""):
                msgAdios = random.choice(self._POSIBLE_DESPEDIDA) + " " + self.__nombre_conocido
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + self.__nombre_conocido
            else:
                msgAdios = random.choice(self._POSIBLE_DESPEDIDA) + ", pero nunca me dijiste tu nombre"
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " por favor dime tu nombre"

            interact_comando_out = msgAdios

        if (comando=="insultar"):
            msgInsulto = ""

            if (self.__nombre_conocido!=""):
                msgInsulto = random.choice(self._POSIBLE_INSULTO) + " " + self.__nombre_conocido
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + self.__nombre_conocido
            else:
                msgInsulto = random.choice(self._POSIBLE_INSULTO) + ", pero nunca me dijiste tu nombre"
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " por favor dime tu nombre"

            interact_comando_out = msgInsulto


        if (comando=="insultar2"):
            msgInsulto = ""

            if (self.__nombre_conocido!=""):
                msgInsulto = random.choice(self._POSIBLE_INSULTO_MALDITO) + " " + self.__nombre_conocido
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + self.__nombre_conocido
            else:
                msgInsulto = random.choice(self._POSIBLE_INSULTO_MALDITO) + ", pero nunca me dijiste tu nombre"
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " por favor dime tu nombre"

            interact_comando_out = msgInsulto

        if (comando=="insultar3"):
            msgInsulto = ""

            if (self.__nombre_conocido!=""):
                msgInsulto = random.choice(self._POSIBLE_INSULTO_3) + " " + self.__nombre_conocido
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " " + self.__nombre_conocido
            else:
                msgInsulto = random.choice + ", pero nunca me dijiste tu nombre"
                #msgSaludo = random.choice(self._POSIBLE_SALUDO) + " por favor dime tu nombre"

            interact_comando_out = msgInsulto


#contextoColusiones = BasicContext("Contexto Colusiones Chile", "C:/Users/Rene Developer/Desktop/BOTS/FOOD_BOT-MOSTRADORColusionPollos_20191207_CONTENIDO.txt")
#salida = contextoPulga.basicResponse("que sabes de los saqueos")
#print("salida:" + salida)


        return interact_out

    def response_FIX(self,user_response):
        robo_response=self.util.string_FIX_000(user_response)
        return robo_response

    def learn(self,txtRaw):
        cnt = len(txtRaw)
        self.log('learn: ' + str(cnt) + ' caracteres' )
        sent_tokens = nltk.sent_tokenize(txtRaw)# converts to list of sentences 
        self.log('learn: ' + str(len (sent_tokens)) + ' sentencias' )
        word_tokens = nltk.word_tokenize(txtRaw)# converts to list of words
        self.log('learn: ' + str(len (word_tokens)) + ' palabras' )

    def eatTxtFile(self,txtSrc):
        f=open(txtSrc,'r',errors = 'ignore')
        txtRaw=f.read()
        txtRaw=txtRaw.lower()# minúsculas
        self.learn(txtRaw)

    def httpGet(self,url_):
        salidaHTTP = ""
        headers_Get = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        s = requests.Session()
        r = s.get(url_, headers=headers_Get)
        salidaHTTP = r.text
        return salidaHTTP



    def setDummy(self,dm):
        self.__maxspeed = dm

    def audio_input(self):
        robo_response_audio_TXTFIX=""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Please wait. Calibrating microphone...")
            # listen for 1 second and create the ambient noise energy level
            r.adjust_for_ambient_noise(source, duration=1)
            print("Dime algo por favor")
            audio = r.listen(source,phrase_time_limit=10)

            # recognize speech using Sphinx/Google
            try:
                #response = r.recognize_sphinx(audio)
                response = r.recognize_google(audio, language="es-ES")
                response = response.lower()
                

                robo_response_audio_TXTFIX = response
                #response = audio_TXTFIX(response)
            #continue
                print("creo que dijiste '" + response + "'")
   
            except sr.UnknownValueError:
                print("No puedo entenderte, estás ahí")
                robo_response_audio_TXTFIX = "sin_captura"
            except sr.RequestError as e:
                print("Ocurrió un error_ {0}".format(e))
            
        return robo_response_audio_TXTFIX

    def batch(self,src_):
        batch_out = ""
        self.engine.say("Entrando a modo batch: mi nombre es: " + self.__name)
        self.engine.runAndWait()
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
            mensajeHumano = self.util_String.string_FIX_002(mensajeHumano)
            print("------------------------------------------------------------------------------------------------------------------")
            print("MENSAJE HUMANO:'" + mensajeHumano+"'")
            print("------------------------------------------------------------------------------------------------------------------")
            #mensajeHumano = self.util.string_FIX_002(mensajeHumano)
            if (self.__humanBatchVoice):
                self.vozChange('MSTTS_V110_esES_PabloM')
                #self.engine.setProperty('voice',self.vozId_('MSTTS_V110_esES_PabloM'))

                self.engine_batch.say("" + str(mensajeHumano))
                self.engine_batch.runAndWait()

            mensajeBot = self.interact(mensajeHumano)

            print("RESPUESTA_ROBOT:" + mensajeBot)
            print("------------------------------------------------------------------------------------------------------------------")

            if (self.__hablar):
                self.vozChange('TTS_MS_ES-ES_HELENA_11.0')
                #self.engine.setProperty('voice',self.vozId_('TTS_MS_ES-ES_HELENA_11.0'))
                self.engine.say("" + str(mensajeBot))
                #engine.say("paso 2")
                self.engine.runAndWait()

        return batch_out



    def vozTesting_DISPONIBLES(self):
        voices = self.engine.getProperty('voices')
        print(self.engine)
        for voice in voices:
            #print(voice, voice.id)
            print("FORMATO:'"  + str(self.vozId_minimo(voice.id)) + "'" )
            self.engine.setProperty('voice', voice.id)

            #engine.say("FORMATO: " + str(voice.id) + "hola mundo")

            self.engine.say('Cargando deita')
            self.engine.runAndWait()
            #engine.stop()

    def vozId_minimo(self,id_completo):
        id_=""+id_completo
        id_ = id_.replace("HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\", "")
        return id_

    def vozId_completo(self,id_voz):
        id_ = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\" + id_voz 
        return id_

    def vozChange(self,id_):
        id_completo = self.vozId_completo(id_)
        #print("setVoz(id_=" + id_ + ")-->" + "FORMATO:'"  + id_completo + "'" )
        self.engine.setProperty('voice', id_completo)
        #self.engine.say('Cambiando voz')
        #self.engine.runAndWait()



    def interact_sesion_preguntas(self,comando):
        interact_sesion_preguntas_out = "No sé ejecutar el comando '" + comando 
        #if (__log):print(__name + '-->' + 'interact: ' + str(self.__maxspeed))

        self.engine.say("Entrando a modo sesión de preguntas, para salir, dime Bye!.")

        self.engine.runAndWait()

        flag=True
        #user_response = self.audio_input()
        while(flag==True):
            print("en el ciclo:")

            user_response = self.audio_input()
            while (user_response=="sin_captura"):
                user_response = self.audio_input()

            #user_response=user_response.lower()
            #user_response = response_FIX(user_response + " ")
            #user_response = user_response.strip()

            if(user_response in 'bye' or user_response == "salir" or user_response == "salir de la sesión de preguntas"):
                print("adiosito:" + user_response)
                exit()


            #bot_response = response_JAIME(user_response)
            #sent_tokens.remove(user_response)

            bot_response = self.interact(user_response)

            print("------------------------------------------------------------------------------------------------------------------")
            print("RESPUESTA_ROBOT:" + bot_response)
            print("------------------------------------------------------------------------------------------------------------------")
            self.engine.say("" + str(bot_response))
            #engine.say("paso 2")
            self.engine.runAndWait()

        return interact_sesion_preguntas_out


#txtBOT = BasicVoiceBot("Sócrates")

#txtBOT.load()

#txtBOT.vozTesting_DISPONIBLES()

#txtBOT.interact("hola")

#txtBOT.testVoz()

#txtBOT.interact_sesion_preguntas("hola")

#txtBOT.batch("BATCH_FLOW_PARIS_20191226_RESUMIDO.txt")

#txtBOT.batch("BATCH_FLOW_ENJOY_20191226_RESUMIDO.txt")

#txtBOT.batch("BATCH_FLOW_LIBRO_LOCO_RENE_20200122.txt")



