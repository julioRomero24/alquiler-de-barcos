from barco import Barco


class Deportivo(Barco):
    def __init__(self, matricula, sloran, añoDeFabricacion,velocidadMax):
        super().__init__(matricula, sloran, añoDeFabricacion)
        self.velocidadMax=velocidadMax
    
    def getTipoDebarco(self):
        print('es un deportivo con velocidad maxima de:',self.velocidadMax)