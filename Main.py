from Logica import Logica
from Persistencia import Archivos

class Control():

    def __init__(self)->None:
        self.__config=Archivos.traerConfiguraciones()
        self.__Estaciones=Archivos.traerEstaciones()
        self.__logica=Logica(config=self.__config)

    def crearArchivo(self)->None:
        self.__logica.filtrar(self.__Estaciones)
        cabeceras=['Codigo','Nombre','Precio','# Definicion','Jer Master','Jer Definicion','Jer Precio','Estructura ID','Zona','Punto','RVC','Obj Number']
        productos=self.__logica.getDataRestaurantes()
        Archivos().makeExcel('Productos.xlsx','Todos',cabeceras,productos)

if __name__=="__main__":
    Control().crearArchivo()