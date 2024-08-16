# Ejercio 1

class vehiculos : 
    def movimiento (self) : 
        pass 
    

class avion (vehiculos) :
     def movimiento (self) :
         print ("Vuela")
         

class tren (vehiculos) :
    def movimiento (self) :
        print ("Corre")
        
        
class barco (vehiculos) :
    def movimiento(self):
        print ("Navega")

class moto (vehiculos) :
    def movimiento(self):
        print ("veloz")
        


def decir_movimiento(vehiculo):
    if isinstance(vehiculo, vehiculos):  # Cambio aquí: usar la clase vihiculos
        vehiculo.movimiento()
    else:
        print("Este no es un vehiculo")


        

avion = avion ()
tren = tren ()
barco = barco ()
moto = moto ()
otro_objeto = object()


decir_movimiento (avion)
decir_movimiento (tren)
decir_movimiento (barco)
decir_movimiento (moto)
decir_movimiento(otro_objeto)
