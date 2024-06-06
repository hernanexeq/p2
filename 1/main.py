from GestorProductos import gestorproductos
if __name__=='__main__':
    gp=gestorproductos()
    band=True
    gp.testproductos()
    while band==True:
        print("\nElija una opcion:")
        print("1. Agregar productos al gestor de productos")
        print("2. Dada una posición de la lista: Mostrar por pantalla qué tipo de producto se encuentra almacenado en dicha posición")
        print("3. Mostrar la cantidad de productos de cada tipo.")
        print("4. Recorrer la colección y mostrar para todos los productos: Nombre, país de origen y temperatura de mantenimiento recomendada, e importe de venta.")
        print("5. Salir\n")
        op=int(input("Ingrese opcion a ejecutar: "))
        if op==1:
            gp.agregarnuevoprod()
        elif op==2:
            gp.mostrartipo()
        elif op==3:
            gp.cantt()
        elif op==4:
            gp.mostrartodos()
        elif op==5:
            print("Adios")
            band=False
        else:
            print("Opcion ingresada incorrecta.")