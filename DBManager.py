#Libreria pyodbc: Contiene todo el codigo necesario para manejar la base de datos
#Libreria ftplib: Contiene todo el codigo necesario para manejar la conexion al servidor FTP
import pyodbc
from copy import deepcopy
from datetime import datetime
from datetime import timedelta

#Clase para establecer la conexion con la base de datos
class ManagerDB():
    
    #Traemos la informacion necesaria de las db, desde el metodo constructor
    def __init__(self,driverdb:str,instanciadb:str,database:str,uid:str,pwd:str,encrypt:str)->None:
        self.__driverDB=driverdb
        self.__instanciadb=instanciadb
        self.__database=database
        self.__uid=uid
        self.__pwd=pwd
        self.__encrypt=encrypt

 
    #Funcion encargada de realizar la conexion a cada estacion y retornar true si se establece la conexion o retornar false si no se establece dicha conexion
    def conectar_Estacion(self,ipcaps)->tuple:
        try:
            self.__conect=pyodbc.connect(f'DRIVER={self.__driverDB};'+
                                            f'SERVER={ipcaps}{self.__instanciadb};'+
                                            f'DATABASE={self.__database};'+
                                            f'UID={self.__uid};'+
                                            f'PWD={self.__pwd};'+
                                            f'ENCRYPT={self.__encrypt}')
            return (True,None)
        except Exception as e:return (False,e)

    #Funcion para realizar consultas en la base de datos
    def consulta_Estacion(self,query:str)->tuple:
        try:
            with self.__conect.cursor() as cursor:
                cursor.execute(query)
                aux=cursor.fetchall()
            consulta=deepcopy(aux)
            return (True,consulta)
        except Exception as e: return (False,e)

    def cerrarConexion(self):self.__conect.close()
    