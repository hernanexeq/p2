from Producto import Producto
from Refrigerados import refrigerados
from Congelados import congelados
from datetime import datetime
import csv
class gestorproductos(object):
    __lista: list

    def __init__(self):
        self.__lista=[]

    def agregarprod(self,unproducto):
        self.__lista.append(unproducto)

    def testproductos(self):
        archivo=open('productos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                if fila[0]=='C':
                    unprod=congelados(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
                else:
                    unprod=refrigerados(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
                self.agregarprod(unprod)
        archivo.close

    def agregarnuevoprod(self):
        try:
            cod=str(input("Ingrese codigo de producto a agregar (C-Cogelado, R-Refrigerado):"))
            if cod.upper()!='C' and cod.upper()!='R':
                print("Dato no valido")
            else:
                print("Ingrese los siguientes datos: \n")
                nom=input("Nombre: ")
                fechen=input("Fecha de envasado: ")
                fechav=input("Fecha de vencimiento: ")
                temp=float(input("Temperatura de mantenimiento: "))
                paiso=input("Pais de origen: ")
                nlote=input("Numero de Lote: ")
                costoba=float(input("Costo base: "))
                if cod.upper()=='C':
                    print("Porcentaje de: ")
                    nt=int(input("Nitrogeno->"))
                    ox=int(input("Oxigeno->"))
                    dc=int(input("Dioxido de Carbono->"))
                    va=int(input("Vapor de agua->\n"))
                    mc=input("Metodo de congelamiento: ")
                    unproducto=congelados(nom,fechen,fechav,temp,paiso,nlote,costoba,nt,ox,dc,va,mc)
                else:
                    codo=input("Ingrese codigo de organizmo: ")
                    unproducto=refrigerados(nom,fechen,fechav,temp,paiso,nlote,costoba,codo)
                self.agregarprod(unproducto)
        except TypeError:
            print("Se esperaba un letra")

    def mostrartipo(self):
        try:
            lon=int(len(self.__lista))
            pos=int(input("Ingrese una posicion entre 0 y {}: ".format(lon-1)))
            if isinstance(self.__lista[pos],congelados):
                print("El producto que se encuentra en la posicion {} es del tipo Congelados".format(pos))
            else:
                print("El producto que se encuentra en la posicion {} es del tipo Refrigerados".format(pos))
        except IndexError:
            print("La posicion ingresada no se encuentra en el rango de la lista")
        except ValueError:
            print("Se esperaba un numero")

    def cantt(self):
        cantC=0
        cantR=0
        for i in range(len(self.__lista)):
            if isinstance(self.__lista[i],congelados):
                cantC+=1
            else:
                cantR+=1
        print("\nLa cantidad de productos Congelados es de {}".format(cantC))
        print("La cantidad de productos Refrigerados es de {}".format(cantR))

    def tamaño(self):
        tam=len(self.__lista)
        return tam

    def mostrartodos(self):
        for producto in self.__lista:
            print(producto.mostrar_informacion())
