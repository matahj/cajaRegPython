
class Caja:
    estdo = 'off'
    
    def __init__(self):
        self.estado = 'on'

    def getEstado(self):
        return self.estado

    def comprar(self):
        print("Ingresar precio: ")
        priducto = float( input() )



c1 = Caja()
print( c1.getEstado() )
c1.comprar()
