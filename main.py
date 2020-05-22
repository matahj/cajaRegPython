
import CajaReg as cr
import os

c1 = cr.Caja()
print("Estado de la caja: " + c1.getEstado() )

while c1.getEstado() == 'on' :

    #os.system('clear') #limpiar pantalla para Linux.
    print("********************************************************************")
    print("********************************************************************")
    c1.imprimeMenu()

    print("Seleccione opción: ")
    resp = int(input())

    if resp== 1:
        c1.comprar()
    elif resp == 2:
        c1.imprimeNumeroTickets()
    elif resp == 3:
        c1.imprimeTicketPorID()
    elif resp == 4:
        c1.corteCaja()
    elif resp == 5:
        c1.apagar()
    else:
        print("Opción no válida")

    
    

#    print("Nueva Compra (si/no): ")
#    resp = input()
#    if(resp=='no'):
#        c1.apagar()
#    else:
#        pass

#print("Estado de la caja: " + c1.getEstado() )


