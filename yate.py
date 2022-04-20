from barco import Barco
class Yate(Barco):
    def __init__(self, matricula, sloran, añoDeFabricacion,camarotes):
        super().__init__(matricula, sloran, añoDeFabricacion)
     
        self.camarotes=camarotes
    
    def getTipoDebarco(self):
        print('es un yate con ',self.camarotes,' camarotes')
