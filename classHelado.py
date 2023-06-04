from classSabor import Sabor

class Helados:
    __gramos: int
    __precio: int
    __sabor= []
    def __init__(self, gr, pr):
        self.__gramos = gr
        self.__precio = pr
        self.__sabor = []
    
    def addsabor(self, sab):
        self.__sabor.append(sab)
    def getgramos(self):
        return self.__gramos
    def getsabor(self):
        return self.__sabor
    def getprecio(self):
        return self.__precio