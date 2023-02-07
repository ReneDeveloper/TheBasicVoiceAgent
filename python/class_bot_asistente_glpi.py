from class_basic_voice_bot import BasicVoiceBot

class AsistenteGlpi(BasicVoiceBot):
	def __init__(self,name_,file_tag):
		BasicVoiceBot.__init__(self, name_, file_tag)

	def procesa_msg(self,aaa,bbb):
		self.log(f'aaa:{aaa}')
		self.log(f'bbb:{bbb}')


asistenteBot = AsistenteGlpi("Asistente GLPI","GLPI")
asistenteBot.voz_testing_disponibles()
#asistenteBot.voz_change('MSTTS_V110_esMX_RaulMM')
#asistenteBot.set_util_comando_src('commands/COMMAND_DEF_GLPI.json')
#asistenteBot.batch("commands/BATCH_FLOW_GLPI.txt")
#asistenteBot.interact_sesion_preguntas('Hola')