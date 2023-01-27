"""test_glpi_project.py"""

from class_glpi_cli import GlpiUtil

#glpi = GlpiUtil()
#util_glpi = GlpiUtil('3v01u710',"http://localhost:8090/glpi","Ius0rLOCYU8ycF8HDCeWhO43J4L2VoXQinhmvtG2")
util_glpi = GlpiUtil(False)

#utilGLPI.__insert_elemento__('Ticket',{'input':{'entities_id':'2','name': 'desierto limpio oxido','status': '2','date':'2020-01-06 00:00:00'}})
#utilGLPI.__insert_elemento__('Ticket',{'input':{'entities_id':'2','name': 'traslado de gases oxido','status': '2','date':'2020-01-06 00:00:00'}})

def main():
	
	print("debe crear proyecto")
	#id_proyecto_nuevo = utilGLPI.crear_proyecto('TEST_DESDE_PYTHON')
	#id_creado = utilGLPI.__insert_proyecto__('Project',{'input':{'entities_id':'2','name': 'PROJECTO DICTADO POR VOz','status': '2','date':'2020-01-06 00:00:00'}})
	#print(f'id_proyecto_nuevo:{id_proyecto_nuevo}')
	#print("debe listar proyecto")
	#id_LISTADO = utilGLPI.get_proyecto__(27)
	#print(f'listar id:{id_LISTADO}')

	#listado = utilGLPI.get_proyectos_()
	#print(f'listar id:{listado}')
	print("debe renombrar proyecto")
	print("debe cambiarle una categoria al proyecto")
	print("debe cambiarle un parametro al proyecto")
	print("debe crear mysql para el proyecto")
	util_glpi.clone_7zip('mysql')
	print("debe renombrar proyecto")


if __name__ == '__main__':
	main()

