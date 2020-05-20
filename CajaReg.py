class Caja:
    estado = 'off'
    precios = [ [1,10.2], [2,25.6], [3,38.3], [4,46.3], [5,56.7] ]
    tickets = []
    
    def __init__(self):
        self.estado = 'on'

    def getEstado(self):
        return self.estado
    
    def apagar(self):
        print("Apagando caja...")
        self.estado = 'off'
        

    def comprar(self):
        continuar = True
        compra = Compra()

        while(continuar):
            print("idProducto (-1 para finalizar): ")            
            idProducto = int( input() )

            if(idProducto==-1):
                continuar = False
            else:
                index = self.precios.index([2,25.6])
                compra.agregarProducto( self.precios[index] )

        self.tickets.append(compra)

class Compra:
    listaProductos = None
    total = None

    def __init__(self):
        self.listaProductos = []
        self.total = 0

    def agregarProducto(self, producto ):
        self.listaProductos.append( producto )
        self.total += producto[1]
        print("producto",producto[0],"agregado.")
        print("Total = ", self.total)


    ##Get lista productos
    
    ##Get total

