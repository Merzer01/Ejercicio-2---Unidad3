from manejadorSabores import ManejadorS
from classHelado import Helados
from classSabor import Sabor
import os

class ManejadorH:
    __listaH = []
    def __init__(self):
        self.__listaH = []
    
    def venta(self, ms):    #opcion1
        print("REGISTRAR VENTA DE HELADOS")
        band = True
        while band:
            gr = int(input("Ingrese cantidad de gramos (100gr-150gr-250gr-500gr-1000gr): "))
            pr = int(input("Ingrese precio del helado: "))
            cant = int(input("Ingrese cantidad de sabores del helado (Max -> 4): "))
            ms.showS()
            h = Helados(gr, pr)

            for i in range(cant):
                idS = int(input(f"Ingrese ID del sabor ({i+1}): "))
                sab = ms.getsabor(idS-1) #sabor elegido
                h.addsabor(sab) #agrega el sabor al helado
                ms.contS(idS-1) #cuenta cant de veces que el sabor es pedido
            self.__listaH.append(h)
            print("Venta registrada!!!")
            comp = str(input("¿Desea registrar otra venta? (si o no): "))
            os.system('pause')
            os.system('cls')
            if comp == 'no':    #controla si se quiere registrar mas ventas o no
                band = False

    def estimargr(self):    #opcion 3
        idS = int(input("Ingrese numero de sabor: "))
        s = []
        total = 0
        for i in range(len(self.__listaH)):
            s = self.__listaH[i].getsabor() #almacena la lista de sabores de la clase helado
            for j in range(len(s)):
                if idS == s[j].getid():
                    cant = len(s)   #guarda la cantidad de comp de la lista -> mas adelante
                    nomb = s[j].getnombre()
                    d = self.__listaH[i].getgramos()/cant
                    total += d
        print("Se pidieron aprx. {}gr del sabor {} (Id: {})".format(total, nomb, idS))

    def sabxtipo(self): #opcion 4
        tipo = int(input("Ingrese tipo de helado: "))
        sab = []    #lista que almacenara todos los sabores pedidos
        aux = []
        for i in range(len(self.__listaH)):
            if self.__listaH[i].getgramos() == tipo:
                aux = self.__listaH[i].getsabor()
                sab += aux
        
        print("SABORES PEDIDOS PARA HELADOS DE {}gr".format(tipo))
        for i in range(len(sab)):
            print(sab[i])

    
    def recaudacion(self):  #opcion 5
        t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0  #100gr - 150gr - 250gr - 500gr - 1000gr
        for i in range(len(self.__listaH)):
            if self.__listaH[i].getgramos() == 100:
                t1 += self.__listaH[i].getprecio()
            elif self.__listaH[i].getgramos() == 150:
                t2 += self.__listaH[i].getprecio()
            elif self.__listaH[i].getgramos() == 250:
                t3 += self.__listaH[i].getprecio()
            elif self.__listaH[i].getgramos() == 500:
                t4 += self.__listaH[i].getprecio()
            elif self.__listaH[i].getgramos() == 1000:
                t5 += self.__listaH[i].getprecio()
        print('''f
-----------------------------
Gramos      Recaudacion Total
{}gr               {}$
{}gr               {}$
{}gr               {}$
{}gr               {}$
{}gr             {}$
-----------------------------
                   {}$
        '''.format(100, t1, 150, t2, 250, t3, 500, t4, 1000, t5, t1+t2+t3+t4+t5))