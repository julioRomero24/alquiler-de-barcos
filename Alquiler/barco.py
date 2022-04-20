class Barco():

    def __init__(self,matricula,sloran,añoDeFabricacion):
        self.matricula=matricula
        self.sloran=sloran
        self.añoDeFabricacion=añoDeFabricacion

    def getModulo(self):
        return (10*self.sloran)