from Producto import Producto
class congelados(Producto):
    __nt: int
    __ox: int
    __dc: int
    __va: int
    __metodocon: str

    def __init__(self,nom,fechaemv,fechaven,tempdemant,pais,lote,costob,nt,ox,dc,va,met):
        super().__init__(nom,fechaemv,fechaven,tempdemant,pais,lote,costob)
        self.__nt=nt
        self.__ox=ox
        self.__dc=dc
        self.__va=va
        self.__metodocon=met

    def getmetodo(self):
        return self.__metodocon
    
    def calcimp(self):
        if self.__metodocon.lower() == 'mecánico':
            return self.costob * 1.15  # Aumento del 15% para método mecánico
        elif self.__metodocon.lower() == 'criogénico':
            return self.costob * 1.15  # Aumento del 15% para método criogénico