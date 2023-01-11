from glpi import GLPI
import requests, json

AA = "RSILCAS"
NN = "GlpiUtil"
VV = "0.1"
FC = "20230111"

class GlpiUtil:

	__base_url = ""
	__token = ""
	__token_App = ""
	__logActivo = True
	__name__ = ""

	def __init__(self,name_,site_,app_):
		self.log( f"{__name__}")
		self.__name__ = name_
		self.__base_url = site_
		self.__token_App = app_
		self.__login_demo__()

	def log(self,log_):
		if self.__logActivo:
			print( f"{self.__name__}:{log_}" )

	def getTicketPrioridad_Ingepro(self,valorOriginal):
		salidaPrioridad = "sin_tipo"

		self.log("getTicketPrioridad_Ingepro:"++" -->" + valorOriginal + "<--")

		bol_ALTA =  any(string in valorOriginal for string in ["fisura","desgaste","reparación"] )

		if (bol_ALTA):
			salidaPrioridad = "2"

		if (salidaPrioridad!="sin_tipo"):
			self.log("salidaPrioridad encontrada:" + salidaPrioridad)

		return salidaPrioridad


#hacer metodo para getEstado
#CTEC=CERRADO=RESUELTO, ABIER=NUEVO, NOTIP=EN CURSO(ASIGANADA), LIB=ENESPERA=EN CURSO (PLANIFICADA)

	def __login_demo__(self):
		self.log( NN + ":__login_demo__:AUTH_REST" )
		auth = ('USER_AUTO', 'USER_AUTO')
		headers = {'App-Token': self.__token_App,'Content-Type': 'application/json'}
		get_LOGIN = requests.get(self.__base_url + '/apirest.php/initSession', auth=auth, headers=headers)
		respuestaLogin = json.loads(get_LOGIN.text)
		self.__token = respuestaLogin['session_token']


		self.log( NN + ":__login_demo__:self.__token:" +  self.__token)

	def __insert_elemento__(self, elemento_, json_values_):
		self.log( NN + ":__insert_elemento__:elemento_:" +  elemento_)
		headers = { 'Authorization' : 'Token ' + self.__token , 'App-Token': self.__token_App, 'Session-Token': self.__token}
		salidaPost = requests.post( self.__base_url + '/apirest.php/' + elemento_ , json=json_values_, headers=headers)

		respuestaRegistro = json.loads(salidaPost.text)
		self.log (str(respuestaRegistro))
		self.log (str(salidaPost.text))

		idCreado = respuestaRegistro['id']
		print("respuestaRegistro:idCreado:" + str(idCreado))
		rest_post_lectura = requests.get(self.__base_url + '/apirest.php/Ticket/' +  str(idCreado), headers=headers)

		return idCreado

	def __insert_ticketIngepro__(self, json_values_):
		self.log( NN + ":__insert_ticketIngepro__:json_values_:" + str(json_values_))

		name = json_values_['input']['name']

		self.log( "vamos a insertar:" + name )


		json_values_['input']['urgency'] = "5"
		json_values_['input']['impact'] = "5"
		json_values_['input']['priority'] = "5"

		idCreado_ = self.__insert_elemento__('Ticket', json_values_)



utilGLPI = GlpiUtil('3v01u710',"http://localhost:8090/glpi","Ius0rLOCYU8ycF8HDCeWhO43J4L2VoXQinhmvtG2")

utilGLPI.__insert_elemento__('Ticket',{'input':{'entities_id':'2','name': 'fisura en cola de tolva lado izquierdo','status': '2','date':'2020-01-06 00:00:00'}})
utilGLPI.__insert_elemento__('Ticket',{'input':{'entities_id':'2','name': 'desierto limpio oxido','status': '2','date':'2020-01-06 00:00:00'}})
utilGLPI.__insert_elemento__('Ticket',{'input':{'entities_id':'2','name': 'traslado de gases oxido','status': '2','date':'2020-01-06 00:00:00'}})
