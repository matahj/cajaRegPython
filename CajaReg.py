class Caja:

    estado = 'off'
    precios = { 1:10.2, 2:25.6 , 3:38.3, 4:46.3, 5:56.7, 6:67.8 }
    tickets = []
    
    def __init__(self):
        print("Iniciando caja...")
        self.estado = 'on'

    def getEstado(self):
        return self.estado
    
    def apagar(self):
        print("Apagando caja...")
        #Falta guardar registro en un archivo
        self.estado = 'off'
        print("Enter para continuar.")
        input()

    def imprimeMenu(self):
        print("Seleccionar opción:")
        print("     1.-Generar compra")
        print("     2.-Imprimir número de tickets")
        print("     3.-Imprimir ticket por id")
        print("     4.-Corte de caja")
        print("     5.-Apagar caja")
        
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
                compra.agregarProducto( [idProducto,self.precios[idProducto]] )

        self.tickets.append(compra)
        self.imprimeTicket(compra)
        print("  Fin de la compra....")
        print("Enter para continuar.")
        input()

    def imprimeTicket(self,compra):
        print("  Imprimiendo ticket:")
        print("  ***************************")
        print("  *IdProducto :  Precio")

        for p in compra.listaProductos:
            print("  *    ", p[0],":",p[1])
        
        print("  *TOTAL = ",compra.total)
        print("  ***************************")

    def imprimeNumeroTickets(self):
        print("  ************************")
        print("  **Número de tickets: ", len(self.tickets) )
        print("  ************************")
        print("Enter para continuar.")
        input()

    def imprimeTicketPorID(self):
        print("Hay", len(self.tickets), "tickets, seleccione uno:" )
        id = int( input() )

        if id > 0 and id <= len(self.tickets):
            self.imprimeTicket( self.tickets[id-1] )
        else:
            print('Opción no valida')
            
        print("Enter para continuar.")
        input()


    def corteCaja(self):
        total = 0
        for t in self.tickets:
            total += t.getTotal()

        print("  ********************")
        print("     CORTE DE CAJA    ")
        print("     NoTickets =",len(self.tickets) )
        print("         TOTAL =",total )
        print("  ********************")
        print("Enter para continuar.")
        input()


    


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

    def getTotal(self):
        return self.total




