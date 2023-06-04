from classSabor import Sabor
import csv

class ManejadorS:
    __listaS = []
    def __init__(self):
        self.__listaS = []
    
    def readarchivo(self):
        with open ('sabores.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)

            for row in lector:
                d1 = int(row[0])    #ID DEL SABOR
                d2 = str(row[1])    #INGREDIENTES
                d3 = str(row[2])    #NOMBRE
                s = Sabor(d1, d2, d3)
                self.__listaS.append(s)
    
    def getsabor(self, idS):
        return self.__listaS[idS]
    def contS(self, idS):
        self.__listaS[idS].contarS()

    def maxsabor(self): #opcion 2
        self.__listaS.sort()
        for i in range(5):
            print("{} -> {} pedidos".format(self.__listaS[i].getnombre(), self.__listaS[i].getcantped()))


    def showS(self):
        for i in range(len(self.__listaS)):
            print(self.__listaS[i])