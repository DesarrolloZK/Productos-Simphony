from Logica import Logica
from Persistencia import Archivos

class Control():

    def __init__(self)->None:
        self.__config=Archivos.traerConfiguraciones()
        self.__Estaciones=Archivos.traerEstaciones()
        self.__logica=Logica(config=self.__config)

    def crearArchivos(self,ip,punto)->None:
        self.__logica.filtrar(ip)
        cabeceras=['Codigo','Nombre','Precio','# Definicion','Jer Master','Jer Definicion','Jer Precio','Estructura ID','Zona','Punto','RVC','Obj Number']
        productos=self.__logica.getDataRestaurantes()
        Archivos().makeExcel('Productos.xlsx',punto,cabeceras,productos)
    
    def iniciar(self)->None: list(map(lambda x:self.crearArchivos(x["ip"],f'{x["punto"]}-{x["oficina"]}'),self.__Estaciones.values()))

if __name__=="__main__":
    Control().iniciar()