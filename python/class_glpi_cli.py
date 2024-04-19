"""class_glpi_cli.py"""
from glpi import GLPI
import requests, json
import py7zr

AA = "RSILCAS"
NN = "GlpiUtil"
VV = "0.1"
FC = "20230111"

RUTA_CLONES = 'C:/RSILVA_BASIC_BOTS/__BIN_CLONES__/'

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

	def __init__(self,__no_login__):
		self.log( f"__no_login__:{__no_login__}")

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
		auth = ('glpi', 'Admin12345!')
		headers = {'App-Token': self.__token_App,'Content-Type': 'application/json'}
		get_LOGIN = requests.get(self.__base_url + '/apirest.php/initSession', auth=auth, headers=headers)
		respuestaLogin = json.loads(get_LOGIN.text)
		self.__token = respuestaLogin['session_token']
		self.log( NN + ":__login_demo__:self.__token_App:" +  self.__token_App)
		self.log( NN + ":__login_demo__:self.__token:" +  self.__token)


	def get_proyecto__(self, id_proyecto):
		"""function get_proyecto__"""
		self.log( f":get_proyecto__:id_proyecto:{id_proyecto}")
		elemento_ = "Project"

		pars = {}
		pars['id']=id_proyecto
		#pars['expand_dropdowns']=True
		pars['with_tickets']=True
		pars['with_notes']=True
		pars['with_logs']= True

 
		
#		headers = { 'Authorization' : 'Token ' + self.__token , 'App-Token': self.__token_App, 'Session-Token': self.__token}
		headers = { 'App-Token': self.__token_App, 'Session-Token': self.__token}
		print("__get_proyectos_:INICIO:respuestaRegistro:")
		json_values_ = None
		#3salidaPost = requests.get( self.__base_url + '/apirest.php/' + elemento_ , headers=headers)

		#respuestaRegistro = json.loads(salidaPost.text)
		#print("__get_proyectos_:POST:respuestaRegistro:" + str(respuestaRegistro))

		#self.log (str(respuestaRegistro))
		#self.log (str(salidaPost.text))
		
		#idCreado = respuestaRegistro['id']
		#print("respuestaRegistro:idCreado:" + str(idCreado))
		rest_get_lectura = requests.get(self.__base_url + '/apirest.php/Project/' + str(id_proyecto) ,params=pars,headers=headers)

		rest_get_lectura_json = json.loads(rest_get_lectura.text)
		#self.log (str(respuestaElemento))

		url__ = self.__base_url + '/apirest.php/Project/' + str(id_proyecto) + "/ProjectTask/"
		print(f"url__:{url__}")
		print(f"------___________________________________________________")

		pars_tareas = {}
		pars_tareas['projects_id']=id_proyecto
		#pars_tareas['entities_id']=2
		#pars_tareas['projects_id']=23
		print(f"PARAMETROS:{pars_tareas}")

		jsons_tareas = {}
		#jsons_tareas['projects_id']=23



		#pars_tareas['expand_dropdowns']=True

		rest_get_lectura_listado_tareas = requests.get(url__,params=pars_tareas,headers=headers)
		rest_get_lectura_listado_tareas_json = json.loads(rest_get_lectura_listado_tareas.text)

		#self.log (str(salidaPost.text))



		print("RESULTADO DEL ELEMENTO:" + str(rest_get_lectura_json))
		print("------------------------------------------" )
		print("RESULTADO DE TAREAS:" )
		print("------------------------------------------" )
		print( str(rest_get_lectura_listado_tareas_json))
				
		print("------------------------------------------" )



		return "listado de IDs y mas datos"



	def get_proyectos_(self):
		elemento_ = "Project"
		salida = {}

		pars = {}
		pars['id']=5

		self.log( NN + ":__get_proyectos_:elemento_:" +  elemento_)
		headers = { 'Authorization' : 'Token ' + self.__token , 'App-Token': self.__token_App, 'Session-Token': self.__token}
		print("__get_proyectos_:INICIO:respuestaRegistro:")
		json_values_ = {}

		#3salidaPost = requests.get( self.__base_url + '/apirest.php/' + elemento_ , headers=headers)

		#respuestaRegistro = json.loads(salidaPost.text)
		#print("__get_proyectos_:POST:respuestaRegistro:" + str(respuestaRegistro))

		#self.log (str(respuestaRegistro))
		#self.log (str(salidaPost.text))
		
		#idCreado = respuestaRegistro['id']
		#print("respuestaRegistro:idCreado:" + str(idCreado))
		rest_get_lectura = requests.get(self.__base_url + '/apirest.php/Project/' , headers=headers)
		respuestaElemento = json.loads(rest_get_lectura.text)
		self.log (str(respuestaElemento))
		#self.log (str(salidaPost.text))
		print("coso:" + str(respuestaElemento))
		salida = respuestaElemento
		return salida

	def crear_proyecto(self,nombre):
		salida = 'OK'
		id_creado = self.__insert_proyecto__('Project',{'input':{'entities_id':'0','name': nombre,'status': '2','date':'2022-01-15 00:00:00'}})

		print("Salida:{salida}")
		return id_creado

	def __insert_proyecto__(self, elemento_, json_values_):
		self.log( NN + ":__insert_elemento__:elemento_:" +  elemento_)
		headers = { 'Authorization' : 'Token ' + self.__token , 'App-Token': self.__token_App, 'Session-Token': self.__token}
		salidaPost = requests.post( self.__base_url + '/apirest.php/' + elemento_ , json=json_values_, headers=headers)

		respuestaRegistro = json.loads(salidaPost.text)
		self.log (str(respuestaRegistro))
		self.log (str(salidaPost.text))

		idCreado = respuestaRegistro['id']
		print("respuestaRegistro:idCreado:" + str(idCreado))
		#rest_post_lectura = requests.get(self.__base_url + '/apirest.php/Ticket/' +  str(idCreado), headers=headers)
		#print("rest_post_lectura:rest_post_lectura:" + str(rest_post_lectura))
		return idCreado



	def __insert_ticketIngepro__(self, json_values_):
		self.log( NN + ":__insert_ticketIngepro__:json_values_:" + str(json_values_))

		name = json_values_['input']['name']

		self.log( "vamos a insertar:" + name )
		json_values_['input']['urgency'] = "5"
		json_values_['input']['impact'] = "5"
		json_values_['input']['priority'] = "5"

		idCreado_ = self.__insert_elemento__('Ticket', json_values_)


	def clone_XX(self,__tag_name__):
		id_salida = 'ID_NULL'
		ruta_clones = 'C:/RSILVA_BASIC_BOTS/__BIN_CLONES__/XAMPP_743/'
		_7_zip = py7zr.SevenZipFile(f'{ruta_clones}{__tag_name__}.7z', mode='r')
		_7_zip.extractall(path=f'{ruta_clones}mysql_clone')
		#archive.extractall(path="/tmp")
		print(f'_7_zip:{_7_zip}')
		#REVOKE ALL PRIVILEGES ON `glpi1`.* FROM 'glpi1'@'%'; GRANT ALL PRIVILEGES ON `glpi1`.* TO 'glpi1'@'%'; 
		return id_salida

	def clone_glpi(self,__glpi_image__,__tag_name__):
		id_salida = 'ID_NULL'
		__glpi_image__ = 'glpi_M20230126'

		ruta_clones = 'C:/RSILVA_BASIC_BOTS/__BIN_CLONES__/GLPI_FOLDER_VERSIONS/'
		_7_zip = py7zr.SevenZipFile(f'{ruta_clones}{__glpi_image__}.7z', mode='r')
		_7_zip.extractall(path=f'{ruta_clones}mysql_clone')
		#archive.extractall(path="/tmp")
		print(f'_7_zip:{_7_zip}')
		#REVOKE ALL PRIVILEGES ON `glpi1`.* FROM 'glpi1'@'%'; GRANT ALL PRIVILEGES ON `glpi1`.* TO 'glpi1'@'%'; 
		return id_salida

#util_glpi = GlpiUtil(False)

#util_glpi.clone_glpi(None, 'new_glpi_27')

def add_SENSOR(sensor_data_):#http://localhost:8090/glpi/apirest.php
    status_ = "NOK"
    glpi_config = {'baseUrl': 'http://localhost:8090/glpi', 'App-Token': 'Ius0rLOCYU8ycF8HDCeWhO43J4L2VoXQinhmvtG2'}
    auth = ('USER_AUTO', 'USER_AUTO')
    headers = {'App-Token': 'Ius0rLOCYU8ycF8HDCeWhO43J4L2VoXQinhmvtG2','Content-Type': 'application/json'}
    req_login = requests.get(glpi_config['baseUrl'] + '/apirest.php/initSession', auth=auth, headers=headers)
    print (str(req_login))
    respuestaLogin = json.loads(req_login.text)
    print("session_token:" + respuestaLogin['session_token'])
    headers = {'App-Token': glpi_config['App-Token'], 'Session-Token': respuestaLogin['session_token']}
    #sensor_data = {'input': {'name': 'SENSOR DESDE API REST', 'serial': 'N23','entities_id':'1','states_id':'5'}} 
    # states_id: STATUS_DESCONOCIDO 5 STATUS_CORRECTO 4 STATUS_INCORRECTO 3
    req_insert = requests.post(glpi_config['baseUrl'] + '/apirest.php/Peripheral', json=sensor_data_, headers=headers)
    req_insert_JSON = json.loads(req_insert.text)
    idCreado = req_insert_JSON['id']
    return idCreado



from PIL import Image, ImageFont

def generate_logo(__name__):
	#text = "Hello world!"
	font_size = 36
	font_filepath = "/Library/Fonts/Artegra_Sans-600-SemiBold-Italic.otf"
	color = (67, 33, 116, 155)

	font = ImageFont.truetype(font_filepath, size=font_size)
	mask_image = font.getmask(__name__, "L")
	img = Image.new("RGBA", mask_image.size)
	img.im.paste(color, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
	img.save(f'IMAGE{__name__}.png')
	

def generate_logo_glpi(__name__):
	#text = "Hello world!"

	import PIL
	from PIL import ImageFont
	from PIL import Image
	from PIL import ImageDraw
	image_path = "C:/xampp_2022/htdocs/glpi/pics/logos/"
	image_txt = "test_" + __name__

	#image_path = RUTA_CLONES
	#image_name = f"{__name__}_test.png"
	image_name = f"logo-GLPI-100-white.png"
	
	# font = ImageFont.truetype("Arial-Bold.ttf",14)
	font = ImageFont.truetype("c:/windows/fonts/Arial.ttf",14) #msgothic.ttc
	img=Image.new("RGBA", (100,55),(0,0,255))
	draw = ImageDraw.Draw(img)
	draw.text((0, 0),image_txt,(0,0,0),font=font)
	draw = ImageDraw.Draw(img)
	img.save(f"{image_path}{image_name}")

#C:\RSILVA_BASIC_BOTS\__BIN_CLONES__\GLPI_FOLDER_VERSIONS
#C:\xampp_2022\htdocs\glpi\pics


generate_logo_glpi("pepe")