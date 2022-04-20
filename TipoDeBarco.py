from barco import Barco
class TipoDeBarco(Barco):

    def __init__(self,mastiles,potencia,camarotes,deportivo,yate):
        self.mastiles=mastiles
        self.potencia=potencia
        self.camarotes=camarotes
        self.deportivo=deportivo
        self.yate=yate
    
    def getTipoDeBarco(self):
        if (self.camarotes==0):
            return 'deportivo'
        else:
            return 'yate'

    