from barco import Barco
class Alquiler():
    def __init__(self,nombreDeCliente,dni,fechaInicial,fechaFinal,posicionDelAmarre,barco):
        self.nombreDeCliente=nombreDeCliente
        self.dni=dni
        self.fechaInicial=fechaInicial
        self.fechaFinal=fechaFinal
        self.posicionDelAmarre=posicionDelAmarre
        self.barco=barco

    def calcPrecioAlquiler(self):
        if(self.fechaFinal>self.fechaInicial):
            return (((self.fechaFinal-self.fechaInicial)+1)*self.barco.getModulo())
        else:
            return 0
