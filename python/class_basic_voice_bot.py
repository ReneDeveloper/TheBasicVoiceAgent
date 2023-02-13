"""class_basic_voice_bot.py"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# Project: Basic Voice Bot
# Author : Rene Silva
# Email  : rsilcas@outlook.es
# Date   : 2023-02-07
# -----------------------------------------------------------------------------
#
# Description:
#
# This Python script Generates a bot to understand human sentences
# that means: you talk, and the invoke a SpeechToText script to obtain the text
# the bot contains tables or structures to undersatand some keys of that text,
# then the bot based on the keys stored can choose a possible response for the input text
# the basic capabilities can be extended in a new bot class inheriting the basic voice functions
# for example you can create a class_joke_bot like: class JokeBot(BasicVoiceBot):
# all the bots can speak with humans and can simulate the interaction with the batch mode

import random
import nltk #RSILVA_20200305 NATURAL LANGUAGE TOOL KIT
import speech_recognition as sr #RSILVA_20200305 RECONOCIMIENTO DE VOZ ENTRADA
import pyttsx3 #RSILVA_20200305 PYTHON TEXT TO SPEECH
from class_util_string import UtilString
from class_util_command import UtilCommand

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
    voice_actual = voice_engine
    #'MSTTS_V110_esES_PabloM' 'MSTTS_V110_esMX_RaulMM'
    #'TTS_MS_ES-ES_HELENA_11.0'  TTS_MS_ES-MX_SABINA_11.0

    def __init__(self,name_, file_tag):
        """function ____"""
        self.log('BasicVoiceBot:INIT:')
        self.__name = 'Sin configurar bot'
        self.util_string = UtilString()
        self.log('BasicVoiceBot:INIT:SETEANDO COMANDOS POR DEFECTO')
        self.util_command = UtilCommand(file_tag)
        self.__name = name_
        self.engine = pyttsx3.init()
        self.voz_change('TTS_MS_ES-MX_SABINA_11.0')

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

    #def set_util_comando_src(self,src_comandos):
    #    """function ____"""
    #    self.log("set_util_comando_src: " + src_comandos)
    #    util_command = UtilCommand(src_comandos)
    #    #util_command.cargaComandos(src_comandos)
    #    self.__util_command = util_command

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
        self.log(f'mapa_comando:{mapa_comando}')
        return interact_out

    def interact_02_main_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_02_main_main"""
        interact_out = "OK"
        self.log(f'interact_02_main_main:{interact_out:}')
        self.log(f'mapa_comando:{mapa_comando}')
        return interact_out

    def interact_03_post_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_03_post_main"""
        interact_out = "OK"
        self.log(f'interact_03_post_main:{interact_out:}')
        self.log(f'mapa_comando:{mapa_comando}')
        return interact_out

    def new_interact(self,msg):
        """function ____"""
        interact_out = 'No te entiendo, me falta información'
        mapa_comando = self.util_command.getMapaComando(msg)

        out_each = self.new_interact_each(mapa_comando)
        out_each = out_each.lower()
        if any(mapa_comando):
            #self.log('mapa_comando:' + str(mapa_comando))
            for key_comando in mapa_comando:
                #print ("------------------------------------------")
                self.log("key_comando:" + key_comando)
                if key_comando[0:4]=="key_":
                    self.log("es una key de comando:posibles respuestas:VECTOR_[key]'")
                    auto_reponses = mapa_comando[ 'VECTOR_'+key_comando ]
                    if auto_reponses is not None and any(auto_reponses):#si existen responses
                        #self.log("seleccionar una respuesta aleatoria")
                        auto_response_rnd = random.choice(auto_reponses)
                        interact_out = auto_response_rnd

        return interact_out

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
        file_txt=open(txt_src,'r',errors = 'ignore',encoding='utf-8')
        txt_raw=file_txt.read()
        txt_raw=txt_raw.lower()# minúsculas
        self.learn(txt_raw)

    def audio_input(self):
        """function ____"""
        robo_response_audio_txtfixed=""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Please wait. Calibrating microphone...")
            # listen for 1 second and create the ambient noise energy level
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Dime algo por favor")
            audio = recognizer.listen(source,phrase_time_limit=10)

            # recognize speech using Sphinx/Google
            try:
                #response = recognizer.recognize_sphinx(audio, language="es-ES")
                response = recognizer.recognize_google(audio, language="es-ES")
                response = response.lower()
                robo_response_audio_txtfixed = response
                #response = audio_TXTFIX(response)
            #continue
                print("creo que dijiste '" + response + "'")

            except sr.UnknownValueError:
                print("No puedo entenderte, estás ahí")
                robo_response_audio_txtfixed = "sin_captura"
            except sr.RequestError as e_request:
                print(f"Ocurrió un error_ {e_request}")

        return robo_response_audio_txtfixed

    def batch(self,src_):
        """function ____"""
        batch_out = ""
        self.engine.say("Entrando a modo batch: mi nombre es: " + self.__name)
        self.engine.runAndWait()
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
                #print("VOICE")
                #print(f"VOICE:self.engine:{self.engine}")
                #time.sleep(0.5)
                self.engine.say("" + str(mensaje_humano))
                #time.sleep(0.5)
                self.engine.runAndWait()

            mensajeBot = self.new_interact(mensaje_humano)

            print("RESPUESTA_ROBOT:" + mensajeBot)
            print("----------------------------------------------------------")

            if self.__hablar:
                self.voz_change(self.voice_engine )
                #'TTS_MS_ES-ES_HELENA_11.0''MSTTS_V110_esES_PabloM'
                #self.engine.setProperty('voice',self.vozId_('TTS_MS_ES-ES_HELENA_11.0'))
                #print("VOICE") print(f"VOICE:self.engine:{self.engine}")     #time.sleep(0.5)
                self.engine.say("" + str(mensajeBot))
                #time.sleep(0.5)                #engine.say("paso 2")
                self.engine.runAndWait()

        return batch_out

    def voz_testing_disponibles(self):
        """function ____"""
        voices = self.engine.getProperty('voices')
        #print(self.engine)
        for voice in voices:
            #print(voice, voice.id)
            print("FORMATO:'"  + str(self.voz_id_minimo(voice.id)) + "'" )
            self.engine.setProperty('voice', voice.id)
            #engine.say("FORMATO: " + str(voice.id) + "hola mundo")
            self.engine.say('Cargando deita')
            self.engine.runAndWait()
            #engine.stop()

    def voz_id_minimo(self,id_completo):
        """function ____"""
        id_voz=""+id_completo
        windows_reg = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\"
        id_voz = id_voz.replace(windows_reg, "")
        return id_voz

    def voz_id_completo(self,id_voz):
        """function ____"""
        id_completo = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\" + id_voz
        return id_completo

    def voz_change(self,id_):
        """function ____"""
        self.log(f"CAMBIANDO VOZ:{id_}")
        if self.voice_actual==id_:
            self.log(f"ES LA MISMA VOZ:{id_}")
            return

        self.log(f"CAMBIANDO VOZ:{id_}")
        self.voice_actual=id_

        id_completo = self.voz_id_completo(id_)
        #print("setVoz(id_=" + id_ + ")-->" + "FORMATO:'"  + id_completo + "'" )
        self.engine.setProperty('voice', id_completo)

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

            if(user_response in 'bye' or user_response == "salir"
                or user_response == "salir de la sesión de preguntas"):
                msg_out = "adiosito, nos vemos en otra sesión"
                self.engine.say(msg_out)
                #engine.say("paso 2")
                self.engine.runAndWait()
                print("adiosito:" + msg_out)
                sys.exit()


            bot_response = self.new_interact(user_response)

            print("----------------------------------------------------------")
            print("RESPUESTA_ROBOT:" + bot_response)
            print("----------------------------------------------------------")

            self.engine.say("" + str(bot_response))
            #engine.say("paso 2")
            self.engine.runAndWait()

        return interact_sesion_preguntas_out
