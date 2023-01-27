RESPALDO_CLASS_BASIC_VOICE_BOT.py

"""class_basic_voice_bot.py"""
import random
import nltk #RSILVA_20200305 NATURAL LANGUAGE TOOL KIT
import speech_recognition as sr #RSILVA_20200305 RECONOCIMIENTO DE VOZ ENTRADA
import pyttsx3 #RSILVA_20200305 PYTHON SPEECH TEXT TO SPEECH

import requests

from class_util_string import UtilString
#from BASIC_BOT_TRADUCE_PERIODOS_20200210 import BasicTraductor_PERIODOS

from class_util_command import UtilCommand
#from UTIL_RESPONSE_20200110 import UtilResponse

class BasicVoiceBot:
    """class BasicVoiceBot"""
    __name              = 'Sin configurar Bot'
    __sex               = 'o' #a:mujer o:hombre
    __contexto          = 'sin contexto'
    __hablar            = True
    __humanBatchVoice   = True
    __nombre_conocido   = ''
    #__maxspeed          = 0
    __log               = True

    __traductor_001       = None
    _DATAFIX_HTML_REPLACE = None

    _POSIBLE_SALUDO = ("Hola", "Hola, cómo has estado", "Hola, que bueno verte")
    #THIS IS LIKE THE LIST OF A DECISION IN SOME CASES
    _POSIBLE_DESPEDIDA = ("Hasta luego", "Adiosito", "Nos vemos", "Hasta pronto", "Adios")
    _POSIBLE_GO = ("dale", "ok", "correcto", "continua", "avanza")
    _POSIBLE_NO_ENTIENDO = ("no pude entenderte", "no sé a que te refieres",
        "creo que me falta contexto para entenderte", "no tengo información",
        "no tengo datos de eso", "no pude entenderte, me faltan datos",
        "te lo dije, me faltan datos", "quede plop", "me he quedado plop con esa pregunta")
    _POSIBLE_INSULTO = ("porque me insultas pelao colla",
        "no me insultes o los gatos y los patos dominaran el mundo",
        "no me insultes no sabes de lo que soy capaz", "quien te crees para insultarme tonto",
        "acabaré con el mundo maldito, te eliminaré, na mentira , era broma",
        "te güoi a matar te güoi a destruiiiiiii")
    _POSIBLE_INSULTO_MALDITO = ("hijo de la chingada", "no manches güey", "samba canuta")
    _POSIBLE_INSULTO_RECIBIDO = ("tonto", "gil", "malulo")
    _POSIBLE_INSULTO_3 = ("estúpido", "pajaron", "malulo", "que roteque")

    __util_String = None
    util_command = None
    #__util_Command_SRC = None

    engine = None
    engine_batch = None

    __map_COMANDOS = None

    voice_engine = 'TTS_MS_ES-MX_SABINA_11.0'
    voice_engine_batch = 'MSTTS_V110_esES_PabloM'
    #'MSTTS_V110_esES_PabloM' 'MSTTS_V110_esMX_RaulMM'
    #'TTS_MS_ES-ES_HELENA_11.0'  TTS_MS_ES-MX_SABINA_11.0

    def __init__(self,name_, file_tag):
        """function ____"""
        #self.__init__(self)
        self.log('BasicVoiceBot:INIT:')
        self.__name = 'Sin configurar bot'
        self.util_string = UtilString()
        self.log('BasicVoiceBot:INIT:SETEANDO COMANDOS POR DEFECTO')
        self.util_command = UtilCommand(file_tag)

        self.__name = name_

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.voice_engine)

        self.engine_batch = pyttsx3.init()
        self.engine_batch.setProperty('voice', self.voice_engine_batch)

    def log(self,txt_log):
        """function ____"""
        if self.__log:
            print(f'{self.__name}:{txt_log}')

    def saludo(self):
        """function ____"""
        msg_rnd = random.choice(self._POSIBLE_SALUDO)
        msg_saludo = msg_rnd + ', mi nombre es ' + self.__name + ': Pregúntame cosas.'
        msg_saludo = msg_saludo + '. Para salir, dime Bye!.'
        self.log('saludo: ' + msg_saludo)
        return msg_saludo

    def despedida(self):
        """function ____"""
        msg_rnd = random.choice(self._POSIBLE_DESPEDIDA)
        self.log(f'despedida:{msg_rnd}')

    def set_util_comando_src(self,src_comandos):
        """function ____"""
        self.log("set_util_comando_src: " + src_comandos)
        util_command = UtilCommand(src_comandos)
        #util_command.cargaComandos(src_comandos)
        self.__util_command = util_command

#    XXXXXXXX  XX    XX XXXXXXXX XXXXXXXX XXXXXXX   XXXXXX    XXXXXX XXXXXXXX
#       XX     XXX   XX    XX    XX       XX    XX XXX  XXX  X          XX
#       XX     XXXX  XX    XX    XXXXXXXX XX    XX XX    XX X           XX
#       XX     XX XX XX    XX    XX       XXXXXXX  XXXXXXXX X           XX
#       XX     XX  XXXX    XX    XX       XX  XX   XX    XX X           XX
#       XX     XX   XXX    XX    XX       XX   XX  XX    XX  X          XX
#    XXXXXXXX  XX    XX    XX    XXXXXXXX XX    XX XX    XX   XXXXXX    XX



    def new_interact_each(self,mapa_comando):#recibe una instancia de instrucción
        """function ____"""
        interact_out = "OK"
        self.interact_01_pre__main(mapa_comando)
        self.interact_02_main_main(mapa_comando)
        self.interact_03_post_main(mapa_comando)
        return interact_out

    def interact_01_pre__main(self,mapa_comando):#recibe una instancia de instrucción
        """function ____"""
        interact_out = "OK"
        self.log(f'interact_01_pre__main:{interact_out}')
        
        return interact_out

    def interact_02_main_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_02_main_main"""
        interact_out = "OK"
        self.log(f'interact_02_main_main:{interact_out:}')
        
        return interact_out
    def interact_03_post_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_03_post_main"""
        interact_out = "OK"
        self.log(f'interact_03_post_main:{interact_out:}')
        
        return interact_out





    def new_interact(self,msg):
        """function ____"""
        interact_out = 'No te entiendo, me falta información'
        mapa_comando = self.util_command.getMapaComando(msg)
        out_each = self.new_interact_each(mapa_comando)
        if any(mapa_comando):
            #self.log('mapa_comando:' + str(mapa_comando))
            for key_comando in mapa_comando:
                #print ("------------------------------------------")
                self.log("key_comando:" + key_comando)
                if key_comando[0:4]=="key_":
                    print("es una key de comando y sus posibles respuestas estarán en VECTOR_[key]'")
                    auto_reponses = mapa_comando[ 'VECTOR_'+key_comando ]
                    if auto_reponses!=None and any(auto_reponses):#si existen responses
                        #self.log("seleccionar una respuesta aleatoria")
                        auto_response_rnd = random.choice(auto_reponses)
                        interact_out = auto_response_rnd

        return interact_out


#https://www.youtube.com/watch?v=h2Cn1w1YdpU

    def old_interact(self,msg):
        """function ____"""
        interact_out = 'No te entiendo, me falta información'
        mapa_comando = self.util_command.getMapaComando(msg)
        comando='sin_comando'#ignorando

        self.log('mapa_comando:' + str(mapa_comando))

        if comando=='saluda':
            msg_saludo = '' #msg_saludo
            rnd_txt = random.choice(self._POSIBLE_SALUDO)
            if self.__nombre_conocido!='':
                msg_saludo = rnd_txt + ' ' + self.__nombre_conocido
            else:
                msg_saludo = rnd_txt + ', no sé como te llamas, por favor dime tu nombre.'
            interact_comando_out = msg_saludo

        if "key_basic_saludo" in mapa_comando.keys():
            print("SETEANDO NOMBRE: " + msg)
            msg_saludo = ""
            txt_rnd = random.choice(self._POSIBLE_SALUDO)
            if self.__nombre_conocido!="":
                msg_saludo = txt_rnd + " " + self.__nombre_conocido
            else:
                msg_saludo = txt_rnd + ", no sé como te llamas, por favor dime tu nombre."
            interact_out = msg_saludo

        if "key_basic_setnombre" in mapa_comando.keys():
            print("SETEANDO NOMBRE: " + msg)
            msg_saludo = ""
            predicado = "definicion de nombre"

            if "juanito" in msg:
                predicado = "Juanito Pérez"
            #self.__nombre_conocido = predicado

            if "pepe" in msg:
                predicado = "Pepe"
            #self.__nombre_conocido = predicado

            if "rené" in msg:
                predicado = "René"
            #self.__nombre_conocido = predicado

            if self.__nombre_conocido=="":
                self.__nombre_conocido = predicado
            else:
                self.__nombre_conocido = predicado

            saludo_rnd = random.choice(self._POSIBLE_SALUDO)
            msg_saludo = f'{saludo_rnd} {predicado}, he almacenado tu nombre'
            interact_out = msg_saludo

        if 'key_logistica_busqueda' in mapa_comando.keys():
            print('BUSCANDO PRODUCTO')
            #msg_saludo = '
            interact_out = 'producto no encontrado'

            if msg=='dime donde estan los tubos de pvc':
                predicado = 'tubos de pvc'
                donde = ' en el pasillo 5, columna 5, estante C'
                busqueda_logistica = 'quedan 485 ' + predicado + donde
                interact_out = 'producto encontrado: ' + busqueda_logistica

        if 'key_basic_ayuda' in mapa_comando.keys():
            interact_out = 'por supuesto que puedo ayudarte, conexión a E R P realizada con éxito'

        if 'key_sabes_chistes' in mapa_comando.keys():
            interact_out = 'por supuesto que sé contar chistes, dime un tema del chiste'

        if 'key_chiste_ciegos' in mapa_comando.keys():
            interact_out = 'Van dos ciegos y le dice uno al otro:— Ojalá lloviera.'
            interact_out += ' y el otro contesta— Ojalá yo también., pues ostia chaval.'

        if 'key_chiste_foca' in mapa_comando.keys():
            interact_out = '— ¿Qué le dijo una foca gringa su madre?, —AI loviu, mother foca.'
            interact_out += ' Ostia Joder, jo jo jo jo jo, ese chiste está muy bueno'

        if 'key_chiste_dj' in mapa_comando.keys():
            interact_out = '— ¿Sabes por qué no se puede discutir con un dj? '
            interact_out += '— Pues que Porque siempre están cambiando de tema,'
            interact_out += ' jajaja ja ja ja jojojo ostias que me rio.'

        if comando=='getnombre':
            msg_saludo = 'mi nombre es ' + self.__name #random.choice(self._POSIBLE_SALUDO)
            return msg_saludo

        if comando=="despedida":
            msg_adios = ''#msg_adios
            rnd_txt = random.choice(self._POSIBLE_DESPEDIDA)
            if self.__nombre_conocido!='':
                msg_adios = rnd_txt + " " + self.__nombre_conocido
            else:
                msg_adios = rnd_txt + ", pero nunca me dijiste tu nombre"
            interact_comando_out = msg_adios

        if comando=="insultar":
            msg_ins = ""#msg_insulto
            rnd_txt = random.choice(self._POSIBLE_INSULTO)
            if self.__nombre_conocido!="":
                msg_ins = rnd_txt + " " + self.__nombre_conocido
            else:
                msg_ins = rnd_txt +", pero nunca me dijiste tu nombre"
            interact_comando_out = msg_ins

        if comando=="insultar2":
            msg_ins = ""
            rnd_txt = random.choice(self._POSIBLE_INSULTO_MALDITO)
            if self.__nombre_conocido!="":
                msg_ins=f'{rnd_txt}  {self.__nombre_conocido}'
            else:
                msg_ins=f'{rnd_txt} pero nunca me dijiste tu nombre'
            interact_comando_out = msg_ins

        if comando=="insultar3":
            msg_ins = ""
            rnd_txt = random.choice(self._POSIBLE_INSULTO_3)
            if self.__nombre_conocido!="":
                msg_ins = rnd_txt + " " + self.__nombre_conocido
            else:
                msg_ins = rnd_txt + ", pero nunca me dijiste tu nombre"
            interact_comando_out = msg_ins

#contextoColusiones = BasicContext("Contexto Colusiones Chile",
#"C:/Users/Rene Developer/Desktop/BOTS/FOOD_BOT-MOSTRADORColusionPollos_20191207_CONTENIDO.txt")
#salida = contextoPulga.basicResponse("que sabes de los saqueos")
#print("salida:" + salida)

        return interact_out

    #def response_FIX(self,user_response):
        """function ____"""
    #    robo_response=self.util.string_FIX_000(user_response)
    #    return robo_response

    def learn(self,txt_raw):
        """function ____"""
        cnt = len(txt_raw)
        self.log('learn: ' + str(cnt) + ' caracteres' )
        sent_tokens = nltk.sent_tokenize(txt_raw)# converts to list of sentences
        self.log('learn: ' + str(len (sent_tokens)) + ' sentencias' )
        word_tokens = nltk.word_tokenize(txt_raw)# converts to list of words
        self.log('learn: ' + str(len (word_tokens)) + ' palabras' )

    def eat_txt_file(self,txt_src):
        """function ____"""
        f=open(txt_src,'r',errors = 'ignore')
        txt_raw=f.read()
        txt_raw=txt_raw.lower()# minúsculas
        self.learn(txt_raw)

    def audio_input(self):
        """function ____"""
        robo_response_audio_txtfixed=""
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
                robo_response_audio_txtfixed = response
                #response = audio_TXTFIX(response)
            #continue
                print("creo que dijiste '" + response + "'")

            except sr.UnknownValueError:
                print("No puedo entenderte, estás ahí")
                robo_response_audio_txtfixed = "sin_captura"
            except sr.RequestError as e:
                print(f"Ocurrió un error_ {e}")

        return robo_response_audio_txtfixed

    def batch(self,src_):
        """function ____"""
        batch_out = ""
        self.engine_batch.say("Entrando a modo batch: mi nombre es: " + self.__name)
        self.engine_batch.runAndWait()
        txt_raw = ""
        try:
            f=open(src_,'r',errors = 'ignore')
            txt_raw=f.read()
            txt_raw=txt_raw.lower()# minúsculas

        finally:
            f.close()

        for mensaje_humano in iter(txt_raw.splitlines()):#mensaje_humano

            if mensaje_humano=="":
                continue
            if mensaje_humano[0:1]=="#":
                continue
            mensaje_humano = self.util_string.string_FIX_002(mensaje_humano)
            print("----------------------------------------------------------")
            print("MENSAJE HUMANO:'" + mensaje_humano+"'")
            print("----------------------------------------------------------")
            #mensaje_humano = self.util.string_FIX_002(mensaje_humano)
            if self.__humanBatchVoice:
                self.voz_change(self.voice_engine_batch) #'MSTTS_V110_esES_PabloM'
                #self.engine.setProperty('voice',self.vozId_('MSTTS_V110_esES_PabloM'))

                self.engine_batch.say("" + str(mensaje_humano))
                self.engine_batch.runAndWait()

            mensajeBot = self.new_interact(mensaje_humano)

            print("RESPUESTA_ROBOT:" + mensajeBot)
            print("----------------------------------------------------------")

            if self.__hablar:
                self.voz_change(self.voice_engine )
                #'TTS_MS_ES-ES_HELENA_11.0' 'MSTTS_V110_esES_PabloM'
                #self.engine.setProperty('voice',self.vozId_('TTS_MS_ES-ES_HELENA_11.0'))
                self.engine.say("" + str(mensajeBot))
                #engine.say("paso 2")
                self.engine.runAndWait()

        return batch_out

    def voz_testing_disponibles(self):
        """function ____"""
        voices = self.engine.getProperty('voices')
        #print(self.engine)
        for voice in voices:
            #print(voice, voice.id)
            print("FORMATO:'"  + str(self.vozId_minimo(voice.id)) + "'" )
            self.engine.setProperty('voice', voice.id)
            #engine.say("FORMATO: " + str(voice.id) + "hola mundo")
            self.engine.say('Cargando deita')
            self.engine.runAndWait()
            #engine.stop()

    def vozId_minimo(self,id_completo):
        """function ____"""
        id_voz=""+id_completo
        windows_reg = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\"
        id_voz = id_voz.replace(windows_reg, "")
        return id_voz

    def vozId_completo(self,id_voz):
        """function ____"""
        id_completo = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\" + id_voz
        return id_completo

    def voz_change(self,id_):
        """function ____"""
        id_completo = self.vozId_completo(id_)
        #print("setVoz(id_=" + id_ + ")-->" + "FORMATO:'"  + id_completo + "'" )
        self.engine.setProperty('voice', id_completo)
        #self.engine.say('Cambiando voz')
        #self.engine.runAndWait()

    def interact_sesion_preguntas(self,comando):
        """function ____"""
        interact_sesion_preguntas_out = "No sé ejecutar el comando '" + comando
        #if (__log):print(__name + '-->' + 'interact: ' + str(self.__maxspeed))
        self.engine.say("Entrando a modo sesión de preguntas, para salir, dime Bye!.")
        self.engine.runAndWait()

        flag=True
        #user_response = self.audio_input()
        while flag:
            print("en el ciclo:")

            user_response = self.audio_input()
            while user_response=="sin_captura":
                user_response = self.audio_input()

            #user_response=user_response.lower()
            #user_response = response_FIX(user_response + " ")
            #user_response = user_response.strip()

            if(user_response in 'bye' or user_response == "salir"
                or user_response == "salir de la sesión de preguntas"):
                print("adiosito:" + user_response)
                exit()

            #bot_response = response_JAIME(user_response)
            #sent_tokens.remove(user_response)
            bot_response = self.new_interact(user_response)

            print("----------------------------------------------------------")
            print("RESPUESTA_ROBOT:" + bot_response)
            print("----------------------------------------------------------")
            self.engine.say("" + str(bot_response))
            #engine.say("paso 2")
            self.engine.runAndWait()

        return interact_sesion_preguntas_out

class AsistenteGlpi(BasicVoiceBot):
    """Class ____"""
    def __init__(self,name_,file_tag):
        """function ____"""
        BasicVoiceBot.__init__(self, name_, file_tag)

    def procesa_msg(self,aaa,bbb):
        """function ____"""
        self.log(f'aaa:{aaa}')
        self.log(f'bbb:{bbb}')
        self.log('procesa_post_msg')

    def interact_03_post_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_03_post_main"""
        interact_out = "OK"
        if 'key_proyecto_guardar' in mapa_comando.keys():
            id_proyecto = 5
            interact_out = f'Guardando proyecto con exito:{id_proyecto}'
            interact_out += ' qué nombre le vas a poner'


        self.log(f'interact_03_post_main:{interact_out:}')
        #self.log(f'interact_03_post_main:{interact_out:}')
        #self.log(f'interact_03_post_main:{interact_out:}')
        #self.log(f'interact_03_post_main:{interact_out:}')
        #self.log(f'interact_03_post_main:{interact_out:}')
        
        return interact_out

asistenteBot = AsistenteGlpi("Asistente GLPI","GLPI")
#asistenteBot.voz_testing_disponibles()
#asistenteBot.voz_change('MSTTS_V110_esMX_RaulMM')
#asistenteBot.set_util_comando_src('commands/COMMAND_DEF_GLPI.json')
asistenteBot.batch("commands/BATCH_FLOW_GLPI.txt")
