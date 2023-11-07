from DBManager import ManagerDB

class Logica():

    def __init__(self,config:dict)->None:
        self.__db=ManagerDB(config['DriverDB'],config['InstanciaDB'],config['DATABASE'],config['UID'],config['PWD'],config['ENCRYPT'])
        self.__query=config['query']
        self.__codValidos1=[]

    def aux_Filtrar(self,dato)->None:
        if dato[0] not in self.__codValidos1:
            self.__codValidos1.append(dato[0])
            self.__dataRestaurantes.append(tuple(dato))

    def filtrar(self,estaciones:dict)->bool:
        self.__dataRestaurantes=[]
        consultas=[]
        def recorrerEstaciones(ipcaps:str,punto:str)->None:
            nonlocal consultas
            bandera=self.__db.conectar_Estacion(ipcaps)
            print(punto)
            if bandera[0]:
                aux=self.__db.consulta_Estacion(self.__query)
                if aux[0]:consultas+=aux[1]
                else:print(f'{aux[1]}')
                self.__db.cerrarConexion()
            else:print(bandera[1])
        list(map(lambda x:recorrerEstaciones(x["ip"],x["punto"]),estaciones.values()))
        list(map(self.aux_Filtrar,consultas))


    def getDataRestaurantes(self)->tuple: return self.__dataRestaurantes


