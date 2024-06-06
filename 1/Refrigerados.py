from Producto import Producto
from datetime import datetime
class refrigerados(Producto):
    __codor: str
    
    def __init__(self,nom,fechaemv,fechaven,tempdemant,pais,lote,costob,codor):
        super().__init__(nom,fechaemv,fechaven,tempdemant,pais,lote,costob)
        self.__codor= codor

    def calcimp(self):
        fechaactual= datetime.now()
        dif= (self.fechaven.year - fechaactual.year)*12 + (self.fechaven.month - fechaactual.month)
        if dif>2:
                imp=self.costob -(self.costob *10/100)
        else:
                imp=self.costob + (self.costob *1/100)
        return imp