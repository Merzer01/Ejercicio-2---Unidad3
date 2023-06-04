class Sabor:
    __idSabor: int
    __ingredientes: str
    __nombreSabor: str
    __cantPed = 0   #cantidad de veces pedido
    def __init__(self, id=None, ing=None, sab=None):
        self.__idSabor = id
        self.__ingredientes = ing
        self.__nombreSabor = sab
    def __str__(self):
        return ("{} ({})".format(self.__nombreSabor, self.__idSabor))
    
    def __gt__(self, other):
        if self.__cantPed < other.__cantPed:
            return True
        elif self.__cantPed > other.__cantPed:
            return False
        
    def getnombre(self):
        return self.__nombreSabor
    def getcantped(self):
        return self.__cantPed
    def getid(self):
        return self.__idSabor
    def contarS(self):
        self.__cantPed += 1
    def __add__(self, other):
        l = []
        l.append(other)
        return l