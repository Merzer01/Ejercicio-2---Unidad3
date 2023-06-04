from manejadorHelados import ManejadorH
from manejadorSabores import ManejadorS
from classMenu import Menu
import os

if __name__ == '__main__':
    os.system('cls')
    mh = ManejadorH()
    ms = ManejadorS()
    ms.readarchivo()    #carga de los datos
    band = True

    while band:
        menu = Menu()
        opcion = menu.showmenu()
        if opcion == 1:
            mh.venta(ms)
        elif opcion == 2:
            ms.maxsabor()
        elif opcion == 3:
            mh.estimargr()
        elif opcion == 4:
            mh.sabxtipo()
        elif opcion == 5:
            mh.recaudacion()
        elif opcion == 0:
            print("Saliendo...")
            band = False
        else:
            print("Opcion incorrecta")
        os.system('pause')
        os.system('cls')