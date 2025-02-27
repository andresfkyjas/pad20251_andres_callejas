import requests
import json

class Ingestion:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    def obtener_datos_api(self,url="",params={}):
        url = "{}/{}/{}/".format(url,params["coin"],params["method"])
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(error)
            return {}
    
    def guardar_datos(self,datos={},nombre_archivo="ingestion"):
        with open("{}db/{}.json".format(self.ruta_static,nombre_archivo), "w") as archivo:
            json.dump(datos,archivo)
        
    def guardar_db(self,datos={},nombre_archivo="ingestion"):
        pass
    
ingestion = Ingestion()
parametros = {"coin":"BTC","method":"ticker"}
url = "https://www.mercadobitcoin.net/api"
datos = ingestion.obtener_datos_api(url=url, params=parametros)
if len(datos)>0:
    print(json.dumps(datos,indent=4))
else:
    print("no se obtubo la consulta")
ingestion.guardar_datos(datos=datos,nombre_archivo="ingestion")

