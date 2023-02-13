from class_basic_voice_bot import BasicVoiceBot

class AsistenteGlpi(BasicVoiceBot):
    """Class ____"""
    edicion_proyecto_id = "-1"
    edicion_proyecto_name = "Proyecto sin nombre"
    edicion_proyecto_categoria = "Categoria proyecto web"

    proyectos = {}

    def __init__(self,name_,file_tag):
        """function ____"""
        BasicVoiceBot.__init__(self, name_, file_tag)

    def procesa_msg(self,aaa,bbb):
        """function ____"""
        self.log(f'aaa:{aaa}')
        self.log(f'bbb:{bbb}')
        self.log('procesa_post_msg')





    def interact_01_pre__main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_03_post_main"""
        interact_out = "OK"

        self.voz_change(self.voice_engine)

        #self.engine.setProperty('voice', self.voice_engine_batch)#voice_engine_batch
        #self.engine.runAndWait()
        if 'key_idea_insert' in mapa_comando.keys():
            self.log(f'EJECUTANDO:key_idea_insert:{interact_out}')

            #guardar proyecto
            interact_out = f'acá debo guardar una idea'

            self.engine.say(interact_out)
            self.engine.runAndWait()

        #self.voz_change(self.voice_engine)
        return interact_out

    def interact_03_post_main(self,mapa_comando):#recibe una instancia de instrucción
        """function interact_03_post_main"""
        interact_out = "OK"

        self.voz_change(self.voice_engine)

        #self.engine.setProperty('voice', self.voice_engine_batch)#voice_engine_batch
        #self.engine.runAndWait()
        if 'key_proyecto_crear' in mapa_comando.keys():
            self.log(f'EJECUTANDO:key_proyecto_guardar:{interact_out:}')

            #guardar proyecto

            id_proyecto = 27
            self.edicion_proyecto_id = id_proyecto
            interact_out = f'Guardando proyecto con exito:{id_proyecto}'

            self.engine.say(interact_out)
            self.engine.runAndWait()
            interact_out = f'qué nombre le vas a poner al proyecto {id_proyecto}'
            self.engine.say(interact_out)
            self.engine.runAndWait()

        if 'key_proyecto_consulta_categoria' in mapa_comando.keys():
            self.log(f'EJECUTANDO:key_proyecto_consulta_categoria:{interact_out:}')
            interact_out = f' El proyecto :{self.edicion_proyecto_id} es {self.edicion_proyecto_categoria}'
            self.engine.say(interact_out)
            self.engine.runAndWait()

        return interact_out

asistenteBot = AsistenteGlpi("Asistente GLPI","GLPI")
#asistenteBot.voz_testing_disponibles()
#asistenteBot.voz_change('MSTTS_V110_esMX_RaulMM')
#asistenteBot.set_util_comando_src('commands/COMMAND_DEF_GLPI.json')
#asistenteBot.batch("commands/BATCH_FLOW_GLPI.txt")
asistenteBot.interact_sesion_preguntas('Hola')


