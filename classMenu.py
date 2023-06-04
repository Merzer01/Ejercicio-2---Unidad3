class Menu (object):
    def showmenu(self):
        print("MENU DE OPCIONES")
        print("1 - Venta de helado")
        print("2 - Los 5 sabores mas pedidos")
        print("3 - Estimar gramos vendidos por sabor")
        print("4 - Sabores pedidos por tipo de helado")
        print("5 - Importe total recaudado")
        print("0 - SALIR")
        cond = False
        while not cond:
            op = int(input("Ingrese numero de opcion: "))
            if op in [1,2,3,4,5,6,0]:
                cond = True
        return op