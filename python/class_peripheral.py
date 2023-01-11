"""class_peripheral.py"""

from glpi import GLPI
import requests, json

def add_SENSOR(sensor_data_):
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



