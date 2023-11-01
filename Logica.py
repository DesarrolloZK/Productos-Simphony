from DBManager import ManagerDB

class Logica():

    def __init__(self,config:dict)->None:
        self.__db=ManagerDB(config['DriverDB'],config['InstanciaDB'],config['DATABASE'],config['UID'],config['PWD'],config['ENCRYPT'])
        self.__query=config['query']
        self.__condicion1=config['condicion1']
        self.__condicion2=config['condicion2']
        self.__condicion3=config['condicion3']
        self.__condicion4=config['condicion4']
        self.__codValidos1=[]
        self.__codValidos2=[]

    def aux_Filtrar(self,dato)->None:
        if [dato[0],dato[3],dato[8],dato[9],dato[10],dato[11]] not in self.__codValidos1:
            self.__codValidos1.append([dato[0],dato[3],dato[8],dato[9],dato[10],dato[11]])
            if dato[0] not in self.__codValidos2:
                self.__codValidos2.append(dato[0])
                self.__dataRestaurantes.append(tuple(dato))
            elif dato[11]!=None:self.__dataRestaurantes.append(tuple(dato))

    

    def filtrar(self,ipcaps:str)->bool:
        self.__dataRestaurantes=[]
        bandera=self.__db.conectar_Estacion(ipcaps)
        if bandera[0]:
            prio1=self.__db.consulta_Estacion(self.__query+self.__condicion1)
            prio2=self.__db.consulta_Estacion(self.__query+self.__condicion2)
            prio3=self.__db.consulta_Estacion(self.__query+self.__condicion3)
            prio4=self.__db.consulta_Estacion(self.__query+self.__condicion4)
            if prio1[0] and prio2[0] and prio3[0] and prio4[0]: list(map(lambda x:self.aux_Filtrar(x),prio1[1]+prio2[1]+prio3[1]+prio4[1]))
            else:
                print(f'{prio1[1],prio2[1],prio3[1],prio4[1]}')
                return False
        else:
            print(bandera[1])
            return bandera[0]

    def getDataRestaurantes(self)->tuple: return self.__dataRestaurantes


