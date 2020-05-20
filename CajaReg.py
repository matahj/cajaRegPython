class Caja:
    estado = 'off'
    precios2 = { 1:10.2, 2:25.6 , 3:38.3, 4:46.3, 5:56.7, 6:67.8 }
    tickets = []
    
    def __init__(self):
        print("Iniciando caja...")
        self.estado = 'on'

    def getEstado(self):
        return self.estado
    
    def apagar(self):
        print("Apagando caja...")
        self.estado = 'off'
        

    def comprar(self):
        continuar = True
        compra = Compra()

        print("****Iniciando Compra...****")
        while(continuar):
            print("    idProducto (-1 para finalizar): ")            
            idProducto = int( input() )

            if(idProducto==-1):
                continuar = False
            else:
                compra.agregarProducto( [idProducto,self.precios2[idProducto]] )

        self.tickets.append(compra)
        self.imprimeTicket(compra)
        print("  Fin de la compra....")

    def imprimeTicket(self,compra):

        print("  Imprimiendo ticket:")
        print("  ***************************")
        print("  *IdProducto :  Precio")

        for p in compra.listaProductos:
            print("  *     ", p[0],":",p[1])
        
        print("  *TOTAL = ",compra.total)
        print("  ***************************")


    def imprimeMenu(self):

        print("Seleccionar opción:")
        print("     1.-Generar Compra")
        print("     2.-Número de tickets")
        print("     3.-Número de ventas")
        print("     4.-Corte de caja")
        print("     5.-Apagar caja")

    def imprimeNumeroTickets(self):
        print("  ********************")
        print("  **Número de tickets: ", len(self.tickets) )
        print("  ********************")

    def corteCaja(self):
        print("  ********************")
        print("     CORTE DE CAJA    ")
        print("  ********************")



class Compra:
    listaProductos = None
    total = None

    def __init__(self):
        self.listaProductos = []
        self.total = 0

    def agregarProducto(self, producto ):
        self.listaProductos.append( producto )
        self.total += producto[1]
        print("    producto",producto[0],"agregado.")
        print("    Total = ", self.total)




