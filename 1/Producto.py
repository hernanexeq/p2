from datetime import datetime
class Producto(object):
    __nom: str
    __fechaemv: datetime
    fechaven: datetime
    __tempdemant: float
    __pais: str
    __lote: str
    __costobase: float
   
    def __init__(self,nom,fechaemv,fechaven,tempdemant,pais,lote,costob):
        self.__nom=nom
        self.__fechaemv=datetime.strptime(fechaemv,"%d/%m/%Y")
        self.__fechaven=datetime.strptime(fechaven,"%d/%m/%Y")
        self.__tempdemant=tempdemant
        self.__pais=pais
        self.__lote=lote
        self.__costobase=costob

    def getcostobase(self):
        return self.__costobase
    
    def getfechav(self):
        return self.__fechaemv
    
    def getnombre(self):
        return self.__nom
    
    def getpais(self):
        return self.__pais
    
    def gettemp(self):
        return self.__tempdemant

    def calcimp(self):
        pass

    def mostrar_informacion(self):
        info = (
            f"Nombre: {self.__nom}\n"
            f"País de Origen: {self.__pais}\n"
            f"Temperatura Recomendada: {self.__tempdemant}\n"
            f"Importe de Venta: {self.calcimp()}\n"
        )
        return info